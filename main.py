'''COMPARE HYPO'''
from first_hypo import avg_predict
from second_hypo import linear_predict
from third_hypo import time_seg_predict
from data_scraping import time_list, price_list
import matplotlib.pyplot as plt

<<<<<<< HEAD
price_list1 = []
time_list1 = []
for i in range(int(len(price_list) * 0.8)):
    price_list1.append(price_list[i])
    time_list1.append(time_list[i])
=======

test_points = [20, 100, 214, 265]
# plt.plot(test_points, linear_predict(
#     time_list, price_list, test_points), label='Pre Linear Predict')
'''TEST IF THERE IS A DRAMATIC DROP IN PRICE'''
drop = [60, 63, 62, 62.1, 61.5, 61.3]
price_list += drop
time_list += [251 + i for i in range(len(drop))]

>>>>>>> 78178733f1c4cdac3d8cf242697d3a8f84a05342
'''DRAW GRAPH'''
plt.plot(time_list, price_list, 'ro', label='Initial Function')
plt.plot(test_points, avg_predict(time_list1, price_list1,
         test_points), label='Average Predict')
plt.plot(test_points, linear_predict(
<<<<<<< HEAD
    time_list1, price_list1, test_points), label='Linear Predict')
=======
    time_list, price_list, test_points), label='Linear Predict')
plt.plot(test_points, time_seg_predict(
    time_list, price_list, test_points), label='Time Segmented Predict')
>>>>>>> 78178733f1c4cdac3d8cf242697d3a8f84a05342
plt.title('Stock Graph')
plt.legend()
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()
