import numpy as np 
from plotting import *
from calculating import func, derivative

lst_x = np.linspace(-3, 10, num=1000)
lst_y = []

for x in lst_x:
    lst_y.append(func(x))

# print(np.mean(derivative(func, lst_x)))

'''
INPUT = Data scrapped from the web in format (time, price)
OUTPUT = arrays of tuples (x, y) in each interval
'''
# lst_x, lst_y = time, price
'''
EXPLANATION

segment_lst will store value of (x, y) when dydx f(x) = 0,
which also means the max/min value of graph. 

To find a value in the segment_lst, cannot directly check dydx f(x) = 0.
So we will check left and right derivative instead.

If the 2 have opposite signs, there's a dydx f(x) = 0 in the middle. 
Then we will choose the point with derivative nearer to zero.

Between the 2 consecutive maxs/mins, we can assume it is 
a straight line, so we can perform linear regression in this interval.
'''
index = 0
segment_lst = []  # This stores values of (x, y) when f'(x) = 0
output = []
temp_arr = []
prior_element = derivative(func, lst_x)[0]

for element in derivative(func, lst_x):
    temp_arr.append((lst_x[index], lst_y[index]))
    if prior_element * element < 0:
        #compare 2 derivatives and choose the nearer to 0 
        temp = index - 1 if abs(prior_element) < abs(element) else index
        segment_lst.append((lst_x[temp], lst_y[temp]))
        prior_element = element
        output.append(temp_arr)
        temp_arr = []
    if index == len(lst_x) - 1:
        output.append(temp_arr)
    else: 
        index += 1

# print(derivative(func, lst_x))
# print(segment_lst)
# print(derivative(func, segment_lst[0]))

#Draw Graph
graph(lst_x, lst_y, 'Initial Function')
graph(lst_x, derivative(func, lst_x), 'Derivative')
# for element in segment_lst:
#     vertical_line(element[0])

setup_graph()
print(output)