import requests

# API Key for Alpha Vantage
API_KEY = 'P3KXL2CTSG3A7N29'
BASE_URL = 'https://www.alphavantage.co/query'

# Portfolio dictionary to store stock symbols and their quantity
portfolio = {}

def get_stock_price(symbol):
    """Fetch the current price of the stock from the API."""
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    try:
        # Extract the latest closing price from the response
        last_refreshed = data['Meta Data']['3. Last Refreshed']
        price = float(data['Time Series (1min)'][last_refreshed]['4. close'])
        return price
    except KeyError:
        print(f"Error fetching data for {symbol}. Please check the symbol and try again.")
        return None

def add_stock(symbol, quantity):
    """Add a stock to the portfolio."""
    portfolio[symbol] = portfolio.get(symbol, 0) + quantity
    print(f"Added {quantity} shares of {symbol} to your portfolio.\n")

def remove_stock(symbol, quantity):
    """Remove a stock from the portfolio."""
    if symbol in portfolio:
        if portfolio[symbol] <= quantity:
            del portfolio[symbol]
            print(f"Removed {symbol} from your portfolio.\n")
        else:
            portfolio[symbol] -= quantity
            print(f"Removed {quantity} shares of {symbol} from your portfolio.\n")
    else:
        print(f"{symbol} is not in your portfolio.\n")

def show_portfolio():
    """Display the current portfolio and its performance."""
    print("\nYour Portfolio:")
    total_value = 0.0
    for symbol, quantity in portfolio.items():
        price = get_stock_price(symbol)
        if price:
            value = price * quantity
            total_value += value
            print(f"{symbol}: {quantity} shares @ ${price:.2f} = ${value:.2f}")
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

# Main loop to interact with the user
while True:
    print("Stock Portfolio Tracker")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. Show Portfolio")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        symbol = input("Enter the stock symbol: ").upper()
        quantity = int(input("Enter the quantity: "))
        add_stock(symbol, quantity)
    elif choice == '2':
        symbol = input("Enter the stock symbol: ").upper()
        quantity = int(input("Enter the quantity to remove: "))
        remove_stock(symbol, quantity)
    elif choice == '3':
        show_portfolio()
    elif choice == '4':
        print("Exiting the portfolio tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
