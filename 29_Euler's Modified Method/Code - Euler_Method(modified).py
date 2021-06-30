# Code to find approximation of a ordinary differential equation by Euler's (modified) Method

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


def predict(x, y, h, func):
    y = y + h*f(x, y, func)
    return y


def correct(x, y, x1, y1, h, func):
    e = 0.00001
    y1_c = y1
    while(abs(y1_c-y1) > e):
        y1 = y1_c
        y1_c = y + 0.5*h*(f(x, y, func) + f(x1, y1, func))
    return y1_c


def eulerMethodModified(func, x0, y0, xn, n, h):
    result = dict()
    if n != 0:
        h = (xn-x0)/n
    x = x0
    y = y0
    result[x] = y
    while(x < xn):
        next_x = x + h
        next_y_p = predict(x, y, h, func)
        next_y_c = correct(x, y, next_x, next_y_p, h, func)
        x = next_x
        y = next_y_c
        result[x] = y
    return result


if __name__ == "__main__":
    func = parseCompile(input("Enter Function : "))
    x0 = float(input("\nEnter initial x0 : "))
    y0 = float(input("\nEnter initial y0 : "))
    xn = float(input("\nEnter Xn : "))
    print("\n\nEnter 1 for compute with partition n ")
    print("Enter 2 for compute with step-size h ")
    num = int(input("Enter: "))
    if num == 1:
        n = int(input("\nEnter number of partition : "))
        table = eulerMethodModified(func, x0, y0, xn, n, 0)
    else:
        h = float(input("Enter step-size h : "))
        table = eulerMethodModified(func, x0, y0, xn, 0, h)

    print(table)
    for item in table.items():
        print(item)
