# Dictionary of stock symbols and their prices
stock_dictionary = {
    "AAPL": "187.65",
    "GOOG": "136.93",
    "NFLX": "434.67",
    "AMZN": "135.07",
    "META": "295.10",
    "VZ": "34.64",
    "WFC": "41.54",
    "AMD": "106.59",
    "GME": "18.40",
    "NVDA": "492.64"
}

# User inputs stock symbol to check price
stock_symbol = input("Please enter your stock symbol: ").upper()

# Checks if input is in the dictionary and pulls stock price if in the dictionary
stock_check = stock_dictionary.get(stock_symbol)

# Checks if stock symbol is found or not and displays the correct message to the user
if stock_check is None:
    print()
    print(f"Stock {stock_symbol} not found.")
else:
    print()
    print(f"Stock {stock_symbol} price per share: ${stock_check}")