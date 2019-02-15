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

#User inputs for month and year to get file and import file
get_month = input("Which month's sales data would you like to view? Please enter in MM format. ")
get_year = input("For which year? Please enter in YYYY format. ")

#Also based on sales-reporting exercise (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/6d21451ea2d8f992fb067d28ccb37ce37219017d/exercises/sales-reporting/pandas_explore.py)
CSV_FILENAME = "sales-"+"get_month"+"get_year"+ ".csv"
CSV_FILEPATH = os.path.join("data/", CSV_FILENAME)

#Check file validity (if it is there)
#Used: https://www.cyberciti.biz/faq/python-file-exists-examples/
Valid_file = os.path.isfile(CSV_FILEPATH)
if Valid_file == False:
    print("The file you're looking for doesn't seem to be there. Please check that a correctly titled file exists in the data folder and try again!")
#code to process file
else:
    monthlydata = pd.read_csv(CSV_FILEPATH)

#Sort products
#Referenced same exec dash starter code as well as https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
total_sales = monthlydata["sales price"].sum()

numproducts = monthlydata.groupby(["product"]).sum()

numproducts = numproducts.sort_values("sales price", ascending=False)

#Referenced same exec dash starter code (https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales.py)
top_sold = []
ranking = 1 #counter variable
for i, row in numproducts.iterrows():
    p = {"rank": ranking, "name": row.name, "montly_sales": row["sales price"]}
    top_sold.append(p)
    ranking = ranking + 1
 
product_names_list = [p["name"] for p in top_sold]
product_sales_sorted = [p["monthly_sales"] for p in top_sold]
bar_labels = [to_usd(p["monthly_sales"]) for p in told_sold]

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