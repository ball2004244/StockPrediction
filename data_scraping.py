import pandas as pd

df = pd.read_excel('Stock.xlsx', sheetname=0) # can also index sheet by name or fetch all sheets
price_list = df['Closed'].tolist()

time_list = []
for i in range(len(price_list)):
    time_list.append(i+1)
