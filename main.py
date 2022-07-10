import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

'''Init'''
X = np.array([147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]).reshape(-1, 1)
Y = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

# formula for linear reg: y = slope * x + bias
linreg = LinearRegression()
linreg.fit(X, Y)

slope = linreg.coef_
bias = linreg.intercept_
# print(slope)
# print(bias)

'''TESTING WITH NEW POINTS'''
pred_X = np.array([153, 120, 200, 190]).reshape(-1, 1)
pred_Y = linreg.predict(pred_X)
print(pred_Y)

'''DRAW GRAPH'''
plt.plot(X, Y, 'ro')
plt.plot(pred_X, pred_Y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()