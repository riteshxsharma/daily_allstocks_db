import yfinance as yf
from datetime import datetime, timedelta

def get_six_month_average_price(ticker):
    # Calculate the date range for the past 6 months
    end_date = datetime.today()
    start_date = end_date - timedelta(days=182)  # Approximately 6 months

    try:
        # Fetch historical data for the ticker
        stock_data = yf.download(ticker, start=start_date, end=end_date, progress=False)

        if stock_data.empty:
            print(f"No data found for {ticker}.")
            return None

        # Calculate the average closing price over the past 6 months
        avg_price = stock_data['Close'].mean()
        return avg_price

    except Exception as e:
        print(f"An error occurred while processing {ticker}: {e}")
        return None

def main():
    # Input stock tickers from the user, separated by commas
    tickers_input = input("Enter up to 10 stock tickers separated by commas (e.g., AAPL, MSFT, GOOGL): ").strip()
    tickers = [ticker.strip().upper() for ticker in tickers_input.split(',')[:10]]  # Limit to a maximum of 10 tickers

    # Iterate over each ticker to get the average price
    print("\nAverage 6-Month Prices:")
    for ticker in tickers:
        avg_price = get_six_month_average_price(ticker)
        if avg_price is not None:
            print(f"{ticker}: ${avg_price:.2f}")

if __name__ == "__main__":
    main()
