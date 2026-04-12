# Prom.ua GraphQL Scraper

This is a robust Python scraper designed to interact with the **Prom.ua GraphQL API**. It automates the process of extracting product information from catalog categories and exports the results into a structured Excel format.

## 🚀 Key Features
* **GraphQL Integration:** Directly communicates with the site's internal API for high-speed data retrieval.
* **Automated Pagination:** Uses `offset` logic to bypass the single-request limit (50 items) and collect hundreds of products.
* **Anti-Bot Protection:** Implements randomized request delays and browser-like headers to minimize detection.
* **Data Cleaning:** Automatic duplicate removal based on unique Product IDs.
* **Secure Configuration:** Uses `.env` files to keep sensitive session data (cookies) private.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Libraries:** `requests`, `pandas`, `python-dotenv`, `openpyxl`

## 📋 Data Extracted
The scraper captures the following fields for each product:
* `id`: Unique product identifier.
* `name`: Full product title as shown in the catalog.
* `price`: Current listing price.
* `currency`: Localized currency symbol (₴).
* `vendor`: Name of the company/store selling the item.

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/prom-scraper.git](https://github.com/yourusername/prom-scraper.git)
   cd prom-scraper
