# monthly_sales.py
# TODO: import some modules and/or packages here
#referenced Plotly tutorial at: https://plot.ly/~notebook_demo/84/plotting-from-csv-data-csv-or-comma-del/#/
import plotly.plotly as py
import plotly.graph_objs as go #referenced https://plot.ly/python/getting-started/#initialization-for-offline-plotting
import pandas as pd
import os #referenced Prof. Rossetti's notes on os module (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/d42b75d4f536ebeca5d6b1934926cdd95aeea714/notes/python/modules/os.md)


# TODO: write some Python code here to produce the desired functionality...
#used Prof. Rossetti's starter code to convert to USD format (https://github.com/s2t2/exec-dash-starter-py/commit/525446a5850d211bb78dfe1cb3ffb42ea4b3c9ad)

def to_usd(price):
    return"${0:, .2f}".format(price)

#month_lookup function and CSV file lookup based on sales-reporting exercise (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/6d21451ea2d8f992fb067d28ccb37ce37219017d/exercises/sales-reporting/pandas_explore.py)
def month_lookup(month):
	month_MM={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return month_MM[month]

get_month = input("Which month's sales data would you like to view? Please enter in MM format.")
get_year = input("For which year? Please enter in YYYY format.")


CSV_FILENAME = "sales-"+"get_month"+"get_year"+ ".csv"
CSV_FILEPATH = os.path.join("data", CSV_FILENAME)

# 

print("-----------------------")
print("MONTH: March 2018") #To Do: get actual month/year


print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------") #To Do: calculate sales
print("TOTAL MONTHLY SALES: $12,000.71") 


print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.") #To do: retrieve top selling products

print("-----------------------")
print("VISUALIZING THE DATA...")

#To do: add bar chart of top sellers