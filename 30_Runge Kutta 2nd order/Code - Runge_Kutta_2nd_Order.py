# Code to find approximation of a ordinary differential equation by Runge Kutta 2nd order method.
from math import *

def f(x, y, function):
    return eval(function)


def parseCompile(equation):
    if 'e^' in equation:
        equation = equation.replace('e^', 'exp')
    if '^' in equation:
        equation = equation.replace('^', '**')
    print(f"equation: {equation}")
    return equation

def rungeKutta_2(func, x0, y0, xn, n, h):
    result = dict()
    if n!=0:
        h = (xn-x0)/n
    x = x0
    y = y0  
    
    while(x<=xn):
        result[x] = y
        k1 = h*f(x, y, func)
        x = x + h
        k2 = h*f(x, y+k1, func)
        y = y + 0.5*(k1+k2)
    return result    


if __name__ == "__main__":
    func = parseCompile(input("Enter Function : "))
    x0 = float(input("\nEnter initial x0 : "))
    y0 = float(input("\nEnter initial y0 : "))
    xn = float(input("\nEnter Xn : "))
    print("\n\nEnter 1 for compute with partition n ")
    print("Enter 2 for compute with step-size h ")
    num = int(input("Enter: "))
    if num==1:
        n = int(input("\nEnter number of partition : "))
        table = rungeKutta_2(func, x0, y0, xn, n, 0)
    else:
        h = float(input("Enter step-size h : "))    
        table = rungeKutta_2(func, x0, y0, xn, 0, h)


    print(table)
    for item in table.items():
        print(item)