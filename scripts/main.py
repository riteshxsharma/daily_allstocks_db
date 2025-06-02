# main.py

import stock_price_average
import load_data_into_allstocksml

def main():
    choice = input("Choose an option: 1 - Stock Price Average, 2 - Process Data: ")

    if choice == '1':
        ticker = input("Enter the stock ticker (e.g., AAPL, MSFT, GOOGL): ").strip().upper()
        avg_price = stock_price_average.get_six_month_average_price(ticker)

        if avg_price is not None:
            print(f"\nAverage 6-Month Price for {ticker}: ${avg_price:.2f}")

    elif choice == '2':
        load_data_into_allstocksml.process_data()

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
