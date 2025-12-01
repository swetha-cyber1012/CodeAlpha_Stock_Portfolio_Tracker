import csv
from datetime import datetime

# ---------------------------
# Hardcoded Stock Prices
# ---------------------------
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "META": 290
}

# Portfolio dictionary to store user stocks
portfolio = {}

# ---------------------------
# Function: Add Stock to Portfolio
# ---------------------------
def add_stock():
    symbol = input("Enter Stock Symbol (e.g., AAPL): ").upper()
    if symbol not in stock_prices:
        print("⚠ Stock not available in price list!")
        return
    try:
        quantity = int(input("Enter Quantity: "))
        if quantity <= 0:
            print("⚠ Quantity must be positive!")
            return
    except ValueError:
        print("⚠ Invalid input for quantity!")
        return

    if symbol in portfolio:
        portfolio[symbol] += quantity
    else:
        portfolio[symbol] = quantity

    print(f"✅ Added {quantity} shares of {symbol}")

# ---------------------------
# Function: Remove Stock from Portfolio
# ---------------------------
def remove_stock():
    symbol = input("Enter Stock Symbol to remove: ").upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"🗑 Removed {symbol} from portfolio")
    else:
        print("⚠ Stock not in portfolio!")

# ---------------------------
# Function: Show Portfolio Summary
# ---------------------------
def show_portfolio():
    if not portfolio:
        print("📭 Portfolio is empty.")
        return

    print("\n📊 PORTFOLIO SUMMARY")
    print("-" * 50)
    total_investment = 0

    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        value = price * qty
        total_investment += value
        print(f"{symbol} | Quantity: {qty} | Price: ${price} | Value: ${value}")

    print("-" * 50)
    print(f"💰 TOTAL INVESTMENT VALUE = ${total_investment}\n")

# ---------------------------
# Function: Save Portfolio as TXT
# ---------------------------
def save_as_txt():
    if not portfolio:
        print("📭 Portfolio is empty. Nothing to save.")
        return

    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("PORTFOLIO SUMMARY\n")
        file.write(f"Saved on: {datetime.now()}\n\n")
        total_investment = 0
        for symbol, qty in portfolio.items():
            price = stock_prices[symbol]
            value = price * qty
            total_investment += value
            file.write(f"{symbol} - Quantity: {qty}, Price: ${price}, Value: ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")

    print(f"📄 Portfolio saved to {filename}")

# ---------------------------
# Function: Save Portfolio as CSV
# ---------------------------
def save_as_csv():
    if not portfolio:
        print("📭 Portfolio is empty. Nothing to save.")
        return

    filename = "portfolio_summary.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Symbol", "Quantity", "Price", "Value"])
        total_investment = 0
        for symbol, qty in portfolio.items():
            price = stock_prices[symbol]
            value = price * qty
            total_investment += value
            writer.writerow([symbol, qty, price, value])

    print(f"📁 Portfolio saved to {filename}")

# ---------------------------
# Main Menu Function
# ---------------------------
def menu():
    while True:
        print("\n===== 📈 STOCK PORTFOLIO TRACKER =====")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio Summary")
        print("4. Save Portfolio as TXT")
        print("5. Save Portfolio as CSV")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            remove_stock()
        elif choice == "3":
            show_portfolio()
        elif choice == "4":
            save_as_txt()
        elif choice == "5":
            save_as_csv()
        elif choice == "6":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# ---------------------------
# Start Program
# ---------------------------
if __name__ == "__main__":
    menu()
