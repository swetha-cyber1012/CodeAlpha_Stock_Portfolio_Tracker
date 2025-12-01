
# 📈 Stock Portfolio Tracker  
A simple Python-based project to track your stock investments using **hardcoded stock prices** and a clean **menu-driven interface**.  
This project is perfect for beginners learning **Python, dictionaries, file handling, and basic arithmetic**.

---

## 🚀 Features
- Add stocks with quantity  
- Remove stocks  
- View detailed portfolio summary  
- Auto-calculate total investment  
- Save portfolio as:
  - 📄 TXT file  
  - 📁 CSV file  
- Fully menu-driven & beginner-friendly  

---

## 🧾 **Hardcoded Stock Prices**
```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "META": 290
}
```

---

## ▶️ How to Run  
1. Install Python (3.10+ recommended)  
2. Save the script as: `stock_portfolio_tracker.py`  
3. Run using:
```
python stock_portfolio_tracker.py
```

---

## 📌 **Sample Program Output**

```
===== 📈 STOCK PORTFOLIO TRACKER =====
1. Add Stock
2. Remove Stock
3. View Portfolio Summary
4. Save Portfolio as TXT
5. Save Portfolio as CSV
6. Exit
Enter your choice: 1

Enter Stock Symbol (e.g., AAPL): AAPL
Enter Quantity: 5
✅ Added 5 shares of AAPL

===== 📈 STOCK PORTFOLIO TRACKER =====
Enter your choice: 3

📊 PORTFOLIO SUMMARY
--------------------------------------------------
AAPL | Quantity: 5 | Price: $180 | Value: $900
--------------------------------------------------
💰 TOTAL INVESTMENT VALUE = $900
```

---

## 💾 Files Generated
### ✔ **portfolio_summary.txt**
Example:
```
PORTFOLIO SUMMARY
Saved on: 2025-01-01 10:15:20

AAPL - Quantity: 5, Price: $180, Value: $900

Total Investment Value: $900
```

### ✔ **portfolio_summary.csv**
Example:
```
Stock Symbol,Quantity,Price,Value
AAPL,5,180,900
```

---

## 🛠 Technologies Used
- Python  
- Dictionaries  
- File Handling (TXT + CSV)  
- Loops & Functions  

---

## 👨‍💻 Author  
Built with ❤️ for Python learners and internship projects.

---

## ⭐ Suggestion  
You can upgrade this project later by adding:
- Live stock price API (yfinance)  
- Graphs using matplotlib  
- SQLite database to store portfolio  

---

Enjoy coding! 🚀
