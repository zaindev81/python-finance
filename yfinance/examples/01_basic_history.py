import yfinance as yf
import argparse
from src.data import fetch_history

def main():
    parser = argparse.ArgumentParser(description="Fetch historical stock data")
    parser.add_argument("--ticker", type=str, default="AAPL", help="Stock ticker symbol")
    parser.add_argument("--period", type=str, default="1mo", help="Time period for historical data")
    args = parser.parse_args()

    ticker_symbol = args.ticker

    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period=args.period)

    print(data)
    print("Latest Close Price:", data["Close"].iloc[-1])

    fetch_history(ticker_symbol, period=args.period)


if __name__ == "__main__":
    main()