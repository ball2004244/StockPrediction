import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from data_scraping import time_list, price_list

'''
2nd Hypo Calculate linreg all over the function
INPUT: Data from data_scraping.py
'''
def linear_predict(list_x, list_y, pred_x):
    '''
    list_x: array of x-value from data
    list_y: array of y-value from data
    pred_x: array of x-value want to predict
    -> return pred_y: array of predicted y-value
    '''
    raw_x, raw_y = list_x, list_y
        
    X = np.array(raw_x).reshape(-1, 1)
    Y = np.array(raw_y)

    # formula for linear reg: y = slope * x + bias
    linreg = LinearRegression()
    linreg.fit(X, Y)

    slope = linreg.coef_
    bias = linreg.intercept_
    pred_x = np.array(pred_x).reshape(-1, 1)
    pred_y = linreg.predict(pred_x)

    return pred_y

if __name__ == '__main__':
    '''TESTING WITH NEW POINTS'''
    test_points = [300, -57]
    
    '''DRAW GRAPH'''
    plt.plot(time_list, price_list, 'ro')
    plt.plot(test_points, linear_predict(time_list, price_list, test_points))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()