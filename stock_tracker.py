stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:

    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:

        quantity = int(input("Enter quantity: "))

        stock_price = stocks[stock_name]

        investment = stock_price * quantity

        total_investment += investment

        print("Investment added:", investment)

    else:
        print("Stock not available.")

print("\nTotal Investment Value:", total_investment)

file = open("portfolio.txt", "w")

file.write("Total Investment Value: " + str(total_investment))

file.close()

print("Portfolio saved to portfolio.txt")