# monthly_sales.py
#referenced Plotly tutorial at: https://plot.ly/~notebook_demo/84/plotting-from-csv-data-csv-or-comma-del/#/
import plotly as py
import plotly.graph_objs as go #referenced https://plot.ly/python/getting-started/#initialization-for-offline-plotting
import pandas as pd
import os #referenced Prof. Rossetti's notes on os module (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/d42b75d4f536ebeca5d6b1934926cdd95aeea714/notes/python/modules/os.md)


#User inputs for month and year to get file and import file
#input function found: https://docs.python.org/3/library/functions.html#input
#try/except explanation used: https://www.ics.uci.edu/~pattis/ICS-31/lectures/tryexcept/tryexcept.txt
#try/except to check for valid input values (used https://www.pythonforbeginners.com/error-handling/python-try-and-except)
#except error type found here (and also somewhat organically, getting that error the first few times that I had that error running my code...): https://docs.python.org/3/library/exceptions.html 
while True:
    try:
        get_month = input("Which month's sales data would you like to view? Please enter in MM format. ")
        get_year = input("For which year? Please enter in YYYY format. ")
        year_month = get_year + get_month

     #Also based on sales-reporting exercise (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/6d21451ea2d8f992fb067d28ccb37ce37219017d/exercises/sales-reporting/pandas_explore.py)
 
        CSV_FILENAME = "sales-"+ get_year + get_month+ ".csv"
   
        CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "data", CSV_FILENAME)
    
        df = pd.read_csv(CSV_FILEPATH)
    except FileNotFoundError:
        print("Oops! There doesn't seem to be a file matching that name. Please check that your file is named in proper format and in a folder named data and try again!")
    else:
        break

#adapted from sales-reporting exercise (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/6d21451ea2d8f992fb067d28ccb37ce37219017d/exercises/sales-reporting/pandas_explore.py))
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
# #Also consulted: http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html
# #Also consulted: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
#Referenced Stack Overflow to get length of object: https://stackoverflow.com/questions/518021/is-arr-len-the-preferred-way-to-get-the-length-of-an-array-in-python
#Iloc and print output adapted from sales-reporting exercise (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/6d21451ea2d8f992fb067d28ccb37ce37219017d/exercises/sales-reporting/pandas_explore.py)
total_count = len(prodsum_sorted)
for i in range(total_count):
    print(str(i+1)+') '+str(prodsum_sorted.iloc[i][0])+" "+"${0:,.2f}".format(prodsum_sorted.iloc[i][1]))

print("-----------------------")

print("VISUALIZING THE DATA...")    
#Referenced: https://plot.ly/python/horizontal-bar-charts/


#tolist() function explanation used: https://stackoverflow.com/questions/23748995/pandas-dataframe-to-list
#tolist() syntax adapted from example on Geeks for Geeks: https://www.geeksforgeeks.org/python-pandas-series-tolist/
product_names_list=prodsum_sorted['product'].tolist()
product_sales_sorted = prodsum_sorted['sales price']
bar_labels = ['${:,.2f}'.format(p) for p in product_sales_sorted] #just iterate through here instead of using for loop before


#Referenced: https://plot.ly/python/getting-started/#initialization-for-offline-plotting
#Referenced: https://plot.ly/python/user-guide/
#Referenced: https://plot.ly/python/bar-charts/
#Referenced: https://plot.ly/python/axes/
#Referenced: https://plot.ly/python/reference/
#Watched video on plotly bar charts: https://www.youtube.com/watch?v=gHXy-qerHj4
#Watched video on plotly bar charts: https://www.youtube.com/watch?v=qgsqt_TApZU
#X-axis label formatting adapted from: https://stackoverflow.com/questions/41582305/python-plotly-format-axis-numbers-as
py.offline.plot({
    "data": [go.Bar(
                x=product_sales_sorted,
                y=product_names_list,
                orientation = 'h',
                text = bar_labels,
                textposition = 'auto',
                )],
    "layout": go.Layout(
            title="Top Selling Products (" + month_lookup(year_month[-2:]) + ' ' + str(year_month[0:4]) + ")", 
            xaxis = dict(tickformat = "$.2f"
            ))
    }, auto_open=True)

# plotly.offline.plot({
   # "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
   # "layout": go.Layout(title="hello world")
# }, auto_open=True)


