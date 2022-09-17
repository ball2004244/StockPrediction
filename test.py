import numpy as np 
from plotting import *
from calculating import func, derivative

lst_x = np.linspace(-20, 20, num=100)
lst_y = []

for x in lst_x:
    lst_y.append(func(x))

# print(np.mean(derivative(func, lst_x)))

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
prior_element = derivative(func, lst_x)[0]
for element in derivative(func, lst_x):
    if prior_element * element < 0:
        #compare 2 derivatives and choose the nearer to 0 
        temp = index - 1 if abs(prior_element) < abs(element) else index
        segment_lst.append((lst_x[temp], lst_y[temp]))
        prior_element = element
    index += 1

print(derivative(func, lst_x))
# print(segment_lst)
# print(derivative(func, segment_lst[0]))

#Draw Graph
graph(lst_x, lst_y, 'Initial Function')
graph(lst_x, derivative(func, lst_x), 'Derivative')
for element in segment_lst:
    vertical_line(element[0])

setup_graph()