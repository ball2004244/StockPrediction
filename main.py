'''COMPARE HYPO'''
from first_hypo import avg_predict
from second_hypo import linear_predict
from third_hypo import time_seg_predict
from data_scraping import time_list, price_list
import matplotlib.pyplot as plt


test_points = [20, 100, 214, 265]
# plt.plot(test_points, linear_predict(
#     time_list, price_list, test_points), label='Pre Linear Predict')
'''TEST IF THERE IS A DRAMATIC DROP IN PRICE'''
drop = [60, 63, 62, 62.1, 61.5, 61.3]
price_list += drop
time_list += [251 + i for i in range(len(drop))]

'''DRAW GRAPH'''
plt.plot(time_list, price_list, 'ro', label='Initial Function')
plt.plot(test_points, avg_predict(time_list, price_list,
         test_points), label='Average Predict')
plt.plot(test_points, linear_predict(
    time_list, price_list, test_points), label='Linear Predict')
plt.plot(test_points, time_seg_predict(
    time_list, price_list, test_points), label='Time Segmented Predict')
plt.title('Stock Graph')
plt.legend()
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()
