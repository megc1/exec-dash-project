#referenced Plotly tutorial at: https://plot.ly/~notebook_demo/84/plotting-from-csv-data-csv-or-comma-del/#/
import operator
#adapted from sales-reporting exercise (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/6d21451ea2d8f992fb067d28ccb37ce37219017d/exercises/sales-reporting/pandas_explore.py))
def month_lookup(month):
	month_MM={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return month_MM[month]

#Basic Challenge: Formatting Prices
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

def get_top_sellers(data):
    prodnames = data["product"]
    unique_products = prodnames.unique()
    unique_products = unique_products.tolist() 
    most_sales = []
    #Approach adapted from  Prof. Rossetti's starter code: https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales_alt.py#L77
    for product in unique_products:
        sameproduct = data[data["product"] == product]
        product_sales = sameproduct["sales price"].sum()
        most_sales.append({"name": product, "monthly sales": product_sales})
    most_sales = sorted(most_sales, key=operator.itemgetter("monthly sales"), reverse=True)
    return most_sales

if __name__ == "__main__":
    import plotly as py
    import plotly.graph_objs as go #referenced https://plot.ly/python/getting-started/#initialization-for-offline-plotting
    import os #referenced Prof. Rossetti's notes on os module (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/d42b75d4f536ebeca5d6b1934926cdd95aeea714/notes/python/modules/os.md)
    import pandas as pd
    print("------------------------------------------")
    print("Welcome to your executive dashboard! Let's take a look at your sales data.")
    print("------------------------------------------")

    #User inputs for month and year to get file and import file
    #input function found: https://docs.python.org/3/library/functions.html#input
    #try/except explanation used: https://www.ics.uci.edu/~pattis/ICS-31/lectures/tryexcept/tryexcept.txt
    #try/except to check for valid input values (used https://www.pythonforbeginners.com/error-handling/python-try-and-except)
    #except error type found here (and also somewhat organically, getting that error the first few times that I had that error running my code...): https://docs.python.org/3/library/exceptions.html 
    
    while True:
        try:
            get_month = input("Which month's sales data would you like to view? Please enter in MM format. ")
            get_year = input("For which year? Please enter in YYYY format. ")
            #Also based on sales-reporting exercise (https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/6d21451ea2d8f992fb067d28ccb37ce37219017d/exercises/sales-reporting/pandas_explore.py)
            CSV_FILENAME = "sales-" + get_year + get_month + ".csv"
            CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "data", CSV_FILENAME)
            df = pd.read_csv(CSV_FILEPATH)
        except FileNotFoundError:
            print("Oops! There doesn't seem to be a file matching that name. Please check that your file is named in proper format and in a folder named data and try again!")
        else:
            break
    
    year_month = get_year + get_month
    
    top_sellers = get_top_sellers(df)
    
    sum_sales = df['sales price'].sum()
    
    ranking = 1 
    for p in top_sellers:
        print("  " + str(ranking) + ") " + p["name"] + ": " + "${0:,.2f}".format(p["monthly sales"]))
        ranking = ranking + 1

    #Output month and top sold
    #debugging help from @crk60 (thank you Carolyn!)
    print("-----------------------")
    print("MONTH: " + month_lookup(year_month[-2:]) + ' ' + str(year_month[0:4])) 
    print("-----------------------")
    print("CRUNCHING THE DATA...")
    print("-----------------------") #To Do: calculate sales
    #http://pandas.pydata.org/pandas-docs/version/0.19/generated/pandas.DataFrame.sort.html
    #Referenced same exec dash starter code & https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
    #used formatting based on Prof. Rossetti's "to_usd" function
    #https://www.geeksforgeeks.org/python-pandas-dataframe-sum/
    print("TOTAL MONTHLY SALES: "+ "${0:,.2f}".format(sum_sales)) 
    print("-----------------------")
    print("TOP SELLING PRODUCTS:")
    print("-----------------------")
    print("VISUALIZING THE DATA...")    
    #Referenced: https://plot.ly/python/horizontal-bar-charts/
    #tolist() function explanation used: https://stackoverflow.com/questions/23748995/pandas-dataframe-to-list
    #tolist() syntax adapted from example on Geeks for Geeks: https://www.geeksforgeeks.org/python-pandas-series-tolist/
    product_names_list=[]
    product_sales_sorted = []
    for t in top_sellers:
        product_names_list.append(t["name"])
        product_sales_sorted.append(t["monthly sales"])   
    bar_labels = [to_usd(a["monthly sales"]) for a in top_sellers] 
    #Referenced: https://plot.ly/python/getting-started/#initialization-for-offline-plotting
    #Referenced: https://plot.ly/python/user-guide/
    #Referenced: https://plot.ly/python/bar-charts/
    #Referenced: https://plot.ly/python/axes/
    #Referenced: https://plot.ly/python/reference/
    #Watched video on plotly bar charts: https://www.youtube.com/watch?v=gHXy-qerHj4
    #Watched video on plotly bar charts: https://www.youtube.com/watch?v=qgsqt_TApZU
    #X-axis label formatting adapted from: https://stackoverflow.com/questions/41582305/python-plotly-format-axis-numbers-as
    py.offline.plot({
        "data" : [go.Bar(
                    x=product_sales_sorted,
                    y=product_names_list,
                    orientation = 'h',
                    text = bar_labels,
                    textposition = 'auto',                   
                    )],
        "layout" : go.Layout(title="Top Selling Products (" + month_lookup(year_month[-2:]) + ' ' + str(year_month[0:4]) + ")", 
                    xaxis = dict(title = "Sales in USD",
                    tickformat = "$.2f"),
                    yaxis = dict(title = "Products"),
                    #Margin adapted and slightly shrunk down from from https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales.py
                    margin = go.layout.Margin(l=150, pad=12
                )
            )
        }, auto_open=True)


