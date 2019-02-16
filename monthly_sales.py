# monthly_sales.py
# TODO: import some modules and/or packages here
#referenced Plotly tutorial at: https://plot.ly/~notebook_demo/84/plotting-from-csv-data-csv-or-comma-del/#/
import plotly as py
import plotly.graph_objs as go #referenced https://plot.ly/python/getting-started/#initialization-for-offline-plotting
import pandas as pd
import os #referenced Prof. Rossetti's notes on os module (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/d42b75d4f536ebeca5d6b1934926cdd95aeea714/notes/python/modules/os.md)


#User inputs for month and year to get file and import file
#input function found: https://docs.python.org/3/library/functions.html#input
get_month = input("Which month's sales data would you like to view? Please enter in MM format. ")
get_year = input("For which year? Please enter in YYYY format. ")
year_month = get_year + get_month

#try/except to check for valid input values (used https://www.pythonforbeginners.com/error-handling/python-try-and-except)
#except error type found on Stack Overflow: https://stackoverflow.com/questions/28633555/how-to-handle-filenotfounderror-when-try-except-ioerror-does-not-catch-it
#Also based on sales-reporting exercise (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/6d21451ea2d8f992fb067d28ccb37ce37219017d/exercises/sales-reporting/pandas_explore.py)

#try: 
CSV_FILENAME = "sales-"+ get_year + get_month+ ".csv"
   
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "data", CSV_FILENAME)
    
df = pd.read_csv(CSV_FILEPATH)

#adapted from sales-reporting exercise
def month_lookup(month):
	month_MM={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return month_MM[month]

#Output month and top sold
#debugging help from @crk60 (thank you Carolyn!)
print("-----------------------")
print("MONTH: " + month_lookup(year_month[-2:]) + ' ' + str(year_month[0:4])) 

print("-----------------------")
print("CRUNCHING THE DATA...")

#Pandas group-by and sum function: https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum/39923815
prodsum = df.groupby(df['product'], as_index=False).sum()

#http://pandas.pydata.org/pandas-docs/version/0.19/generated/pandas.DataFrame.sort.html
prodsum_sorted = prodsum.sort_values(['sales price'], ascending=False)

print("-----------------------") #To Do: calculate sales
#http://pandas.pydata.org/pandas-docs/version/0.19/generated/pandas.DataFrame.sort.html
#Referenced same exec dash starter code & https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
#used formatting based on Prof. Rossetti's "to_usd" function
#https://www.geeksforgeeks.org/python-pandas-dataframe-sum/
SumSales = df['sales price'].sum()
print("TOTAL MONTHLY SALES: "+ "${0:,.2f}".format(SumSales)) 

print("-----------------------")

print("TOP SELLING PRODUCTS:")
most_sales = []
ranking = 1 #counter variable
#Referenced same exec dash starter code to get iterrows function (https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales.py)
for i, row in prodsum_sorted.iterrows():
    p = {"rank": ranking, "name": row.name, "montly_sales": row["sales price"]}
    most_sales.append(p)
    ranking = ranking + 1
for p in most_sales:
    print(" " + str(p["rank"]) + ") " + p["name"] + ": " + "${0:,.2f}".format(p["monthly_sales"]))

print("-----------------------")

    

    


# month_lookup function and CSV file lookup based on sales-reporting exercise (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/6d21451ea2d8f992fb067d28ccb37ce37219017d/exercises/sales-reporting/pandas_explore.py)
 









print("VISUALIZING THE DATA...")

#To do: add bar chart of top sellers


product_names_list = [p["name"] for p in most_sales]
product_sales_sorted = [p["monthly_sales"] for p in most_sales]
bar_labels = [to_usd(p["monthly_sales"]) for p in most_sales]

#TODO: print bar chart

#TODO: edit formatting

  




#except OSError:
#print("The file you're looking for doesn't seem to be there. Please check that a correctly titled file exists in the data folder and try again!")
