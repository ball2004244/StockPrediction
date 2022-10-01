'''COMPARE HYPO'''
from first_hypo import avg_predict
from second_hypo import linear_predict
from third_hypo import time_seg_predict
from data_scraping import time_list, price_list
import matplotlib.pyplot as plt


'''TEST IF THERE IS A DRAMATIC DROP IN PRICE'''
# drop = [60, 63, 62, 62.1, 61.5, 61.3]
# price_list += drop
# time_list += [251 + i for i in range(len(drop))]

'''CALCULATE ACCURACY'''
'''
Math expression:
Accuracy at 1 point can be well/bad predict
Average Accuracy = Number of Well Predicts Points/ Total
'''

'''
Code explaination:
Segment the input into 2 lists:
1st has 80% data (training set)
2nd has 20% data (testing set)
'''
# add data to training set
training_price = price_list[:int(len(price_list) * 0.8)]
training_time = time_list[:int(len(time_list) * 0.8)]

# add data to testing set
actual_price = price_list[int(len(price_list) * 0.8):len(price_list)]
test_points = time_list[int(len(time_list) * 0.8):len(time_list)]

# predict price with avg predict
predict_price = avg_predict(training_time, training_price, test_points)

# predict price with lin predict
# predict_price = linear_predict(training_time, training_price, test_points)

# find accuracy
well_predict = []
for i in range(len(test_points)):
    if abs(actual_price[i] - predict_price[i]) < 15:
        well_predict.append(predict_price[i])
avg_accuracy = len(well_predict) / len(test_points) * 100
print('Average Predict Line has accuracy of: {:.2f}%'.format(avg_accuracy))

'''DRAW GRAPH'''
plt.plot(time_list, price_list, 'ro', label='Initial Function')
plt.plot(test_points, avg_predict(time_list, price_list, test_points), label='Average Predict')
plt.plot(test_points, linear_predict(time_list, price_list, test_points), label='Linear Predict')
# plt.plot(time_list, price_list, test_points, label='Linear Predict')
# plt.plot(test_points, time_seg_predict(
#     time_list, price_list, test_points), label='Time Segmented Predict')
ax = plt.gca()
ax.axvline(x=training_time[len(training_time) - 1], color='b')
plt.title('Stock Graph')
plt.legend()
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()
