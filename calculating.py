'''
MATHS EXPRESSIONS
f(x) = (x - 3)^2 + 1
lim x -> lst[0] f(v - x) 
d/dx = lim h -> 0 (f(x + h) - f(x)) / h 
'''
def func(x):
    return x ** 3 + (x - 1) ** 2 - 2

'''
sample variables for limit calculator:
L = [1, 0.999, 0.92, 0.9, 0.8]
v = 3
'''

def limit(func, lst, v):
    res = []
    for x in lst:
        res.append(func(v - x))
    return res

def derivative(func, lst):
    derivative_lst = []
    h = 0.0001
    for x in lst:
        dydx = (func(x + h) - func(x)) / h
        derivative_lst.append(dydx)
    return derivative_lst