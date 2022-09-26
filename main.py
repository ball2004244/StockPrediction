'''COMPARE 1st and 2nd HYPO'''
from first_hypo import avg_predict
from second_hypo import linear_predict
from data_scraping import time_list, price_list
import matplotlib.pyplot as plt

price_list1 = []
time_list1 = []
for i in range(int(len(price_list) * 0.8)):
    price_list1.append(price_list[i])
    time_list1.append(time_list[i])
'''DRAW GRAPH'''
test_points = [20, -57, 100, -9, 214]
plt.plot(time_list, price_list, 'ro', label='Initial Function')
plt.plot(test_points, avg_predict(time_list1, price_list1,
         test_points), label='Average Predict')
plt.plot(test_points, linear_predict(
    time_list1, price_list1, test_points), label='Linear Predict')
plt.title('Stock Graph')
plt.legend()
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()
