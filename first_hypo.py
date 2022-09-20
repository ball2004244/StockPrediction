import numpy as np 
import matplotlib.pyplot as plt
from data_scraping import time_list, price_list
from sklearn.linear_model import LinearRegression

# lst_x = np.linspace(-3, 10, num=1000)
# lst_y = []

# for x in lst_x:
#     lst_y.append(func(x))

# print(np.mean(derivative(func, lst_x)))

def avg_predict(list_x, list_y, input_x):
    '''
    1nd Hypo calculate linreg in each interval, then draw the average line

    INPUT = Data scrapped from the web in format (time, price)
    OUTPUT = [[(), ()], [(), ()]]    
    # arrays of tuples (x, y) in each interval
    '''
    # lst_x, lst_y = time, price
    lst_x, lst_y = list_x, list_y

    # different input
    # lst_x, lst_y = time_list[: len(time_list) // 10], price_list[: len(price_list) // 10]

    '''
    EXPLANATION
    Calculate slope of each inteval by hand 
    slope = (f(b) - f(a)) / (b - a)

    Multiply prior slope with current slope
    if the multiplication < 0 -> change inteval
    Then store x, y values of each point in each interval
    '''
    container = []
    temp_arr_x = []
    temp_arr_y = []
    der_lst = []
    prior_der = 1
    for index in range(len(lst_x) - 1):
        temp_arr_x.append(lst_x[index])
        temp_arr_y.append(lst_y[index])
        der = (lst_y[index + 1] - lst_y[index]) / (lst_x[index + 1] - lst_x[index])
        der_lst.append(der)
        if index == 0:
            prior_der = der
        if prior_der * der < 0:
            prior_der = der
            container.append([temp_arr_x, temp_arr_y])
            temp_arr_x = [lst_x[index]]
            temp_arr_y = [lst_y[index]]

    '''
    AT THIS STEP
    We have a list named "container" with format container = [[[], []], [[], []]]
    Each 2 most inner arrays are the value of Xs and Ys in 1 interval
    Now we need to use linreg runs through each interval
    '''
    output = []
    pred_x = np.array(input_x).reshape(-1, 1)

    for interval in container:
        temp_arr = []
        raw_x, raw_y = interval[0], interval[1]
        X = np.array(raw_x).reshape(-1, 1)
        Y = np.array(raw_y)
        # formula for linear reg: y = slope * x + bias
        linreg = LinearRegression()
        linreg.fit(X, Y)

        slope = linreg.coef_
        bias = linreg.intercept_

        '''REFORMAT output'''
            
        pred_y = linreg.predict(pred_x)
        for element in pred_y:
            temp_arr.append(element)
        output.append(temp_arr)
    # plt.plot(pred_x, pred_y)

    '''CALCULATE avg y-value'''
    avg_y = []
    for index in range(len(pred_x)):
        total = 0
        count = 0
        for arr in output:
            total += arr[index]
            count += 1
        avg_y.append(total / count)

    return avg_y


if __name__ == '__main__':
    '''TESTING WITH NEW POINTS'''
    test_points = [300, -57]

    '''DRAW GRAPH'''
    plt.plot(time_list, price_list, 'ro')
    plt.plot(test_points, avg_predict(time_list, price_list, test_points))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
