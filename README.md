# 📦 Prom.ua GraphQL Scraper | API Edition

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GraphQL](https://img.shields.io/badge/API-GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Speed](https://img.shields.io/badge/Speed-Ultra_Fast-success?style=for-the-badge)

**Високопродуктивний скрипт для збору товарів через внутрішній GraphQL API Prom.ua.** Працює напряму з даними, що робить його в десятки разів швидшим та стабільнішим за звичайний HTML-парсинг.

---

### 🚀 Ключові переваги

* **⚡️ GraphQL Power**: Отримує "чисті" JSON-дані без зайвого HTML-сміття. Це мінімізує трафік та час обробки.
* **🔄 Smart Pagination**: Автоматичний перебір товарів через систему `offset`, що дозволяє збирати тисячі позицій за один сеанс.
* **🛡 Stealth Mode**: Використання браузерних заголовків та рандомних затримок для обходу анти-фрод систем.
* **💎 Clean Data**: Вбудована перевірка на дублікати за унікальним `ID` товару.
* **📊 Business Ready**: Експорт результатів у формати **Excel (.xlsx)** або **CSV**, повністю готових до імпорту в CRM або маркетплейси.

---

### 📊 Дані, що збираються

| Поле | Опис |
| :--- | :--- |
| **Product ID** | Унікальний ідентифікатор товару |
| **Назва** | Повне найменування лоту |
| **Ціна** | Актуальна вартість (numeric) |
| **Валюта** | Тип валюти (UAH, USD тощо) |
| **Продавець** | Назва компанії-магазину на Prom |

---

### 🛠 Технологічний стек

* **Core:** `Python 3.10+`
* **Networking:** `requests` (API interaction)
* **Data Handling:** `Pandas`
* **Security:** `python-dotenv` (для захисту ключів та куків)

---

### 📦 Швидкий старт

1. **Клонуй репозиторій:**
   ```bash
   git clone [https://github.com/yourusername/prom-scraper.git](https://github.com/yourusername/prom-scraper.git)
   cd prom-scraper
