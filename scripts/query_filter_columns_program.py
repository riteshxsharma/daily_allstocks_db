import psycopg2
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import ttk

# Load environment variables from .env file
load_dotenv()

# Database connection setup using environment variables
connection = psycopg2.connect(
    database=os.getenv('DB_NAME'),  # Database name from .env
    user=os.getenv('DB_USER'),  # Database username from .env
    password=os.getenv('DB_PASSWORD'),  # Database password from .env
    host=os.getenv('DB_HOST', 'localhost'),  # Default to localhost if not set
    port=os.getenv('DB_PORT', '5432')  # Default to port 5432 if not set
)
cursor = connection.cursor()

# Dictionary of column data types
column_data_types = {
   	"Order": "integer",
	"Symbol": "varchar(5)",
	"Name": "varchar(25)",
	"Current Price": "numeric(7,2)",
	"Price % Chg": "numeric(5,2)",
	"% Chg YTD": "numeric(6,2)",
	"% Chg Cur Week": "numeric(6,2)",
	"% Chg 1 Month": "numeric(5,1)",
	"Volume (1000s)": "integer",
	"Vol % Chg vs 10-Week": "numeric(6,1)",
	"EPS Rating": "integer",
	"EPS Est Next Yr %": "integer",
	"Pre-tax Margins": "numeric(6,1)",
	"Avg Sales % Chg 6Q": "numeric(7,1)",
	"Avg Sales % Chg 4Q": "numeric(7,1)",
	"Sales % Chg Lst Qtr": "integer",
	"Market Cap (mil)": "numeric(9,1)",
	"ROE": "numeric(10,1)",
	"Price to Sales": "numeric(5,2)",
	"% Off High": "numeric(6,2)",
	"Current Ratio": "numeric(6,2)",
	"EV to FCF": "numeric(6,1)",
	"CF vs EPS % Last Qtr": "numeric(7,1)",
	"Debt %": "integer",
	"PEG": "numeric(5,2)",
	"P/E": "integer",
	"Forward P/E": "integer",
	"Industry Name": "varchar(24)",
	"Price to CF": "numeric(11,2)",
	"Price to Book": "numeric(10,2)",
	"Ind Mkt Val (bil)": "numeric(6,1)",
	"ROE 5-Yr Avg": "numeric(10,1)",
	"LT Debt to Working Cap": "numeric(7,2)",
	"Price $ Chg": "numeric(6,2)",
	"Liab to Assets Lss Ind Median": "varchar(3)",
	"CF vs EPS % Last Yr": "numeric(7,1)",
	"Weekly Closing Range": "numeric(8,4)",
	"Prof Marg Geq Ind Median": "varchar(3)",
	"Op Marg Geq Ind Median": "varchar(3)",
	"Vol % Chg vs 50-Day": "numeric(6,1)",
	"Avg AT Margin 2Q": "numeric(4,1)",
	"Avg AT Margin 4Q": "numeric(5,1)",
	"Avg AT Margin 3Q": "numeric(5,1)",
	"AT Margin": "numeric(5,1)",
	"AT Margin Accel": "varchar(3)",
	"Short Volume": "integer",
	"Yield %": "numeric(4,1)",
	"Shrt Int % Chg": "numeric(5,1)",
	"New CEO 12 Months": "varchar(3)",
	"52-Wk Low": "numeric(7,2)",
	"52-Wk High": "numeric(7,2)",
	"% New Lows in Group": "numeric(4,1)",
	"# New Lows in Group": "varchar(2)",
	"Company Description": "varchar(111)",
	"% New Highs in Group": "numeric(4,1)",
	"# New Highs in Group": "varchar(2)",
	"Shrt Int % of Float": "numeric(4,1)",
	"ADR": "varchar(3)",
	"A/D Rating - Pr Wk": "varchar(2)",
	"Incorp Date": "integer",
	"IPO Date": "integer",
	"Exchange": "varchar(6)",
	"% Chg 12 Months": "numeric(5,1)",
	"% Chg 6 Months": "numeric(5,1)",
	"% Chg 3 Months": "numeric(5,1)",
	"RS Rating": "integer",
	"Ind Group RS": "varchar(2)",
	"SMR Rating": "varchar(1)",
	"Trl 26 Wk % Perf vs S&P 500": "integer",
	"Price vs 21-Day": "numeric(5,1)",
	"Daily Closing Range": "numeric(8,4)",
	"Price vs 10-Day": "numeric(5,1)",
	"Price vs 50-Day": "numeric(5,1)",
	"Price vs 150-Day": "numeric(5,1)",
	"Price vs 200-Day": "numeric(5,1)",
	"10 Day > 21 Day > 50 Day": "varchar(1)",
	"50-Day > 150-Day > 200-Day": "varchar(1)",
	"Current day's Volume greater than previous 5 days' Volume": "varchar(1)",
	"50-Day Avg Vol (1000s)": "integer",
	"Current day's Volume greater than previous 10 days' Volume": "varchar(1)",
	"Current day's Volume greater than previous 20 days' Volume": "varchar(1)",
	"RS Line New High": "varchar(3)",
	"Up/Down Vol": "numeric(3,1)",
	"50-Day Avg $ Vol (1000s)": "integer",
	"RS Line New Low": "varchar(3)",
	"RS Line Within 5% of New High": "varchar(1)",
	"Alpha": "numeric(5,2)",
	"Sales % Chg Lst Yr": "integer",
	"Beta": "numeric(5,2)",
	"Avg True Range": "numeric(6,2)",
	"Enterprise Val (mil)": "numeric(9,1)",
	"Number of Funds": "integer",
	"Funds % Increase": "numeric(5,1)",
	"Funds %": "integer",
	"A/D Rating": "varchar(2)",
	"Shares in Float (1000s)": "integer",
	"Shares (1000s)": "integer",
	"Mgmt %": "integer",
	"Sales Growth 3 Yr": "integer",
	"Sector": "varchar(10)",
	"3-Yr EPS Growth Geq 5-Yr": "varchar(3)",
	"EPS % Chg Last Qtr": "integer",
	"Ind Group Rank": "integer",
	"Sales Accel 2 Qtrs": "varchar(3)",
	"Annual Sales (mil)": "numeric(8,1)",
	"Sales Accel 3 Qtrs": "varchar(3)",
	"Avg Sales % Chg 2Q": "numeric(6,1)",
	"Comp Rating": "integer",
	"EPS % Chg 1 Q Ago (-/+)": "integer",
	"EPS Est Cur Yr %": "integer",
	"EPS Est Cur Qtr %": "integer",
	"EPS Surprise": "numeric(7,1)",
	"Sustainable Growth %": "integer",
	"EPS Trailing 4 Qtrs": "numeric(6,2)",
	"Earnings Stability": "integer",
	"EPS Accel 3 Qtrs": "varchar(3)",
	"EPS Due Date": "integer",
	"EPS Lst Rptd": "integer",
	"Number of Stocks": "integer",
	"Last Mark-up Date": "varchar(10)",
	"Days Vol Short 2 Periods Ago": "numeric(4,1)",
	"Timeliness Rating - Pr Wk": "varchar(1)",
	"Days Vol Short 1 Period Ago": "numeric(4,1)",
	"Days Vol Short Current": "numeric(4,1)",
	"Pr Wk High($)": "numeric(7,2)",
	"Ind Grp Rnk 6 Mo Ago": "integer",
	"Ind Grp Rnk 3 Mo Ago": "integer",
	"Ind Grp Rnk Last Week": "integer",
	"Ex-Dividend Date": "integer",
	"Expected X Dividend Amount": "numeric(4,2)",
	"State": "varchar(2)",
	"City": "varchar(20)",
	"Dividend-Adjusted PEG": "numeric(5,2)",
	"P/E Lss 5-Yr Avg": "varchar(3)",
	"P/E Ratio Rank in Grp": "integer",
	"P/E Percent Rank": "integer",
	"P/E vs S&P 500 P/E (%)": "numeric(8,2)",
	"Avg AT Margin 6Q": "numeric(6,1)",
	"Avg AT Margin 5Q": "numeric(6,1)",
	"EPS % Chg 1 Q Ago": "integer",
	"Timeliness Rating": "varchar(1)",
	"RS 6-Month Rating": "integer",
	"RS 3-Month Rating": "integer",
	"Sponsor Rating": "varchar(1)",
	"Sales Growth 5 Yr": "integer",
	"Avg Sales % Chg 5Q": "numeric(7,1)",
	"Avg Sales % Chg 3Q": "numeric(7,1)",
	"EPS % Chg 3 Q Ago (-/+)": "integer",
	"EPS % Chg 2 Q Ago (-/+)": "integer",
	"EPS % Chg Last Qtr (-/+)": "integer",
	"EPS Lst Yr Gtr EPS 4 Yrs Ago": "varchar(3)",
	"Fiscal EPS 6 Yrs Ago": "numeric(5,2)",
	"Fiscal EPS 5 Yrs Ago": "numeric(6,2)",
	"Fiscal EPS 4 Yrs Ago": "numeric(6,2)",
	"Fiscal EPS 2 Yrs Ago": "numeric(6,2)",
	"Fiscal EPS 1 Yr Ago": "numeric(6,2)",
	"Fiscal EPS Lst Yr": "numeric(6,2)",
	"EPS % Growth 5 Yr Pct Rnk": "integer",
	"EPS % Growth 5 Yr": "integer",
	"EPS % Growth 3 Yr": "integer",
	"EPS % Growth 1 Yr": "integer",
	"EPS % Chg 1 Yr Ago": "integer",
	"EPS % Chg Lst Yr": "integer",
	"EPS Trl 4Q Geq EPS Lst Fiscal Yr": "varchar(3)",
	"EPS Trl 4Q Gtr EPS 4 Yrs Ago": "varchar(3)",
	"Avg EPS % Chg 6Q": "numeric(6,1)",
	"Avg EPS % Chg 5Q": "numeric(6,1)",
	"Avg EPS % Chg 4Q": "numeric(6,1)",
	"Avg EPS % Chg 3Q": "numeric(6,1)",
	"Avg EPS % Chg 2Q": "numeric(6,1)",
	"EPS % Chg Lst Q Gtr 3-Yr Growth": "varchar(3)",
	"EPS % Chg 3 Q Ago": "integer",
	"EPS % Chg 2 Q Ago": "integer"
    # Add more columns as needed
}


def execute_query():
    column = column_var.get()
    operator = operator_var.get()
    value = value_entry.get()
    data_type = column_data_types[column]

    # Validate user input based on data type
    if data_type.startswith("numeric") or data_type.startswith("integer"):
        try:
            value = float(value)
        except ValueError:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Invalid input. Please enter a number.")
            return
    elif data_type.startswith("varchar"):
        value = f"'{value}'"

    # Specify the first 10 columns to return
    columns_to_return = [column] + ["Order", "Symbol", "Name", "Current Price", "Price % Chg", "% Chg YTD",
                                    "% Chg Cur Week", "% Chg 1 Month", "Volume (1000s)", "Vol % Chg vs 10-Week"]
    columns_string = ", ".join([f'"{col}"' for col in columns_to_return])

    query = f'SELECT {columns_string} FROM all_stocks_mldata WHERE "{column}" {operator} {value}'
    try:
        cursor.execute(query)
        results = cursor.fetchall()

        # Format the output to be more readable
        output = ""
        # Add the column names to the output
        column_widths = [20] + [10, 8, 20, 15, 12, 12, 15, 15, 15, 20]  # Specify the width for each column
        for i, col in enumerate(columns_to_return):
            output += col.ljust(column_widths[i]) + " "
        output += "\n"
        output += "-" * 150 + "\n"  # Add a separator line
        for row in results:
            for i, col in enumerate(row):
                output += str(col).ljust(column_widths[i]) + " "
            output += "\n"

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)
    except psycopg2.Error as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, str(e))

root = tk.Tk()
root.title("Stock Database Query")

column_var = tk.StringVar()
operator_var = tk.StringVar()

column_label = tk.Label(root, text="Column:")
column_label.grid(row=0, column=0)

column_option = ttk.OptionMenu(root, column_var, *column_data_types.keys())
column_option.grid(row=0, column=1)

operator_label = tk.Label(root, text="Operator:")
operator_label.grid(row=1, column=0)

operator_option = ttk.OptionMenu(root, operator_var, "=", ">", "<", ">=", "<=")
operator_option.grid(row=1, column=1)

value_label = tk.Label(root, text="Value:")
value_label.grid(row=2, column=0)

value_entry = tk.Entry(root)
value_entry.grid(row=2, column=1)

execute_button = tk.Button(root, text="Execute Query", command=execute_query)
execute_button.grid(row=3, column=0, columnspan=2)

result_text = tk.Text(root, height=50, width=300)
result_text.grid(row=4, column=0, columnspan=2)
# Add a scrollbar to the text box
scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
scrollbar.grid(row=5, column=0, columnspan=2, sticky=tk.EW)

# Configure the text box to use the scrollbar
result_text.config(xscrollcommand=scrollbar.set)
scrollbar.config(command=result_text.xview)

root.mainloop()

# Close database connection
connection.close()