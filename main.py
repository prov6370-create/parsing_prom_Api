import os
import time
import random
import requests
import pandas as pd
from dotenv import load_dotenv

# Завантажуємо дані з файлу .env (наші секретні куки та ID)
load_dotenv()

class PromParser:
    def __init__(self):
        # Точка входу в API Прому
        self.url = 'https://prom.ua/graphql'
        
        # Беремо секрети з оточення (витягуємо з .env)
        self.cookies_str = os.getenv("PROM_COOKIES")
        self.client_id = os.getenv("PROM_CLIENT_ID")
        
        # Заголовки, щоб сайт думав, що ми — звичайний браузер Chrome
        self.base_headers = {
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'referer': 'https://prom.ua/ua/Kuhonnye-plity',
            'x-requested-with': 'XMLHttpRequest' # Кажемо, що це AJAX запит
        }

    def _get_cookies(self):
        """Перетворює довгий рядок кук з браузера у формат словника для Python"""
        if not self.cookies_str:
            return {}
        # Розбиваємо рядок по ';' та '=', прибираємо зайві пробіли
        return {c.split('=')[0].strip(): c.split('=')[1].strip() for c in self.cookies_str.split(';') if '=' in c}

    def fetch_batch(self, limit=50, offset=0):
        """Робить один запит до сервера за пачкою товарів"""
        # Тіло запиту (GraphQL). Тут ми кажемо що саме хочемо отримати
        payload = {
            "operationName": "SpecialForYouBlockQuery",
            "variables": {
                "clientId": self.client_id,
                "limit": limit,     # Скільки штук за раз (макс 50)
                "offset": offset    # З якого товару починати (для пагінації)
            },
            "query": """
            query SpecialForYouBlockQuery($limit: Int, $clientId: String, $offset: Int) {
              personalFeed(client_id: $clientId, limit: $limit, offset: $offset) {
                products {
                  product {
                    id
                    name: nameForCatalog
                    price
                    priceCurrencyLocalized
                    company { name }
                  }
                }
              }
            }
            """
        }

        try:
            # Надсилаємо POST запит
            response = requests.post(
                self.url,
                headers=self.base_headers,
                cookies=self._get_cookies(),
                json=payload,
                timeout=15
            )
            
            # Якщо статус 200 — сервер прийняв нас за свого
            if response.status_code == 200:
                # Витягуємо список продуктів з глибокої структури JSON
                return response.json().get('data', {}).get('personalFeed', {}).get('products', [])
            else:
                print(f"[Error] Сервер відмовив: статус {response.status_code}")
        except Exception as e:
            print(f"[Exception] Помилка мережі: {e}")
        return []

    def run(self, total_count=200):
        """Головний цикл збору даних"""
        all_products = []
        offset = 0

        print(f"Починаємо збір. Ціль: {total_count} товарів.")

        while len(all_products) < total_count:
            print(f"Завантаження товарів з позиції {offset}...")
            batch = self.fetch_batch(offset=offset)

            # Якщо сервер прислав порожній список — виходимо
            if not batch:
                print("Більше товарів немає або доступ обмежено.")
                break

            # Перебираємо кожен товар у пачці та чистимо дані
            for item in batch:
                p = item.get('product', {})
                if p:
                    all_products.append({
                        "id": p.get('id'),
                        "name": p.get('name'),
                        "price": p.get('price'),
                        "currency": p.get('priceCurrencyLocalized'),
                        "vendor": p.get('company', {}).get('name') if p.get('company') else "N/A"
                    })

            # Оновлюємо offset (наступна пачка почнеться там, де закінчилася ця)
            offset += len(batch)
            
            # РАНДОМНА ПАУЗА. Це критично! Щоб Пром не забанив за швидкість.
            wait_time = random.uniform(3.0, 6.0)
            time.sleep(wait_time)

        # Якщо щось зібрали — зберігаємо
        if all_products:
            self._save_data(all_products)

    def _save_data(self, data):
        """Зберігає результат в Excel файл"""
        # Створюємо таблицю (DataFrame)
        df = pd.DataFrame(data)
        
        # Видаляємо дублікати по ID (про всяк випадок)
        df_clean = df.drop_duplicates(subset=['id'])
        
        filename = "prom_export.xlsx"
        # Записуємо в файл без індексів (стовпчик 0, 1, 2...)
        df_clean.to_excel(filename, index=False)
        print(f"Успіх! Зібрано {len(df_clean)} унікальних товарів. Файл: {filename}")

# Точка старту скрипта
if __name__ == "__main__":
    parser = PromParser()
    # Можеш поставити тут 500 або 1000, якщо витримають куки
    parser.run(total_count=100)
