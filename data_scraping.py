import csv
 
# open the file in read mode
filename = open('Stock.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
price_list = []
 
# iterating over each row and append
# values to empty list
for col in file:
    price_list.append(col['Close'])
    

time_list = []
for i in range(len(price_list)):
    time_list.append(i)

print(time_list)
print(price_list)

