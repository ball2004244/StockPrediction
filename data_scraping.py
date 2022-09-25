#import external pandas_datareader library with alias of web
import yfinance as web
import csv
import os
 
#import datetime internal datetime module
#datetime is a Python module
import datetime
 
 # take the input from the user: start date, end date, stock symbol
syear = str(input("start year: "))
smonth = str(input("start month: "))
sday = str(input("start day: "))

eyear = str(input("end year: "))
emonth = str(input("end month: "))
eday = str(input("end day: "))

start_date = syear + "-" + smonth + "-" + sday
end_date = eyear + "-" + emonth + "-" + eday

symbol = input("stock's symbol: ")
#datetime.datetime is a data type within the datetime module

 
#DataReader method name is case sensitive
df = web.download(symbol, start_date, end_date)

# delete current Stock.csv to create new one
# first check whether file exists or not
# calling remove method to delete the csv file
# in remove method you need to pass file name and type

 
#invoke to_csv for df dataframe object from 
#DataReader method in the pandas_datareader library
 
#..\first_yahoo_prices_to_csv_demo.csv must not
#be open in another app, such as Excel 
df.to_csv('Stock.csv')

# open the file in read mode
filename = open('Stock.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
price_list = []
 
# iterating over each row and append
# values to empty list
for col in file:
    price_list.append(float(col['Close']))
    

time_list = []
for i in range(len(price_list)):
    time_list.append(int(i))

#print('Time list: ', time_list)
#print('\n')
#print('Price list: ', price_list)