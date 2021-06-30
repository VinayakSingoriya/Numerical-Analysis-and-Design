#Simpson's 3/8 Rule to compute the difinite integral of a function(in tabular form).
# Input required for this code is : Function

from math import *

def f(x, function):
    return eval(function)


def simpson3_8(a, b, n, func):
    h = (b-a)/n
    sum = f(a,func) + f(b,func)

    for i in range(1, n):
        if (i%3==0):
            sum += 2*f(a+i*h, func)
        else:
            sum += 3*f(a+i*h, func)

    integral = (sum*h*3)/8
    print(f'\n>> Intergral = {integral}\n')       




if __name__ == "__main__":
    func = input("Enter function: ")
    a = float(input("Enter lower Limit : "))
    b = float(input("Enter Upper Limit : "))
    n = int(input("Enter number of sub-intervals : "))
    
    simpson3_8(a, b, n, func)
