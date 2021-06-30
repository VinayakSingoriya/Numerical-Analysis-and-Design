# Trapezoidal rule to compute definite integral of a function(in tabular form)
# Input required : function
from math import *

def f(x, function):
    return eval(function)

def Trapezoidal(a, b, n, func):
    h = (b-a)/n
    sum = f(a,func) + f(b,func)
    for i in range(1, n):
        x = a + i*h
        sum += 2*f(x, func)
    integral = (sum*h)/2
    print(f'\n>> Intergral = {integral}\n')   


if __name__ == "__main__":
    func = input("Enter function: ")
    a = float(input("Enter lower Limit : "))
    b = float(input("Enter Upper Limit : "))
    n = int(input("Enter number of sub-intervals : "))

    Trapezoidal(a, b, n, func)