# Import necessary libraries
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
    # Input stock ticker from the user
    ticker = input("Enter the stock ticker (e.g., AAPL, MSFT, GOOGL): ").strip().upper()

    # Get the average price
    avg_price = get_six_month_average_price(ticker)

    # Output the average 6-month price for the stock
    if avg_price is not None:
        print(f"\nAverage 6-Month Price for {ticker}: ${avg_price:.2f}")

if __name__ == "__main__":
    main()
