# Gaussian Quadrature Formula to compute definite integral of a function
# Input required : function

from math import *


def f(x, function):
    return eval(function)


def parseCompile(equation):
    if 'e^' in equation:
        equation = equation.replace('e^', 'exp')
    if '^' in equation:
        equation = equation.replace('^', '**')
    print(f"equation: {equation}")
    return equation


def gaussianQuadrature(a, b, n, func):
    values = {
        1: {"w1": 2, "x1": 0},
        2: {"w1": 1, "w2": 1, "x1": 0.5773502692, "x2": -0.5773502692},
        3: {"w1": 0.8888888889, "w2": 0.5555555556, "w3": 0.5555555556, "x1": 0, "x2": 0.7745966692, "x3": -0.7745966692},
        4: {"w1": 0.6521451549, "w2": 0.6521451549, "w3": 0.3478548451, "w4": 0.3478548451,
            "x1": 0.3399810436, "x2": -0.3399810436, "x3": 0.8611363116, "x4": -0.8611363116},
        5: {"w1": 0.5688888889, "w2": 0.4786286705, "w3": 0.4786286705,
            "w4": 0.2369268851, "w5": 0.2369268851, "x1": 0, "x2": 0.5384693101, "x3": -0.5384693101, "x4": 0.9061798459, "x5": -0.9061798459},
        6: {"w1": 0.171324492, "w2": 0.360761573, "w3": 0.467913935,
            "w4": 0.467913935, "w5": 0.360761573, "w6": 0.171324492, "x1": -0.932469514, "x2": -0.661209386, "x3": -0.238619186,
            "x4": 0.238619186, "x5": 0.661209386, "x6": 0.932469514},
    }

    p = (a+b)/2
    q = (b-a)/2
    integral = 0.0
    for i in range(1, n+1):
        F = f(p+q*values[n][f'x{i}'], func)
        print(f"F{i} : {F}")
        integral += (values[n][f'w{i}'])*F
        print(f"integral : {integral}")
    integral = q*integral
    print(f'\n>> Intergral = {integral}\n')


if __name__ == "__main__":
    a = float(input("Enter lower limit a : "))
    b = float(input("\nEnter upper limit b : "))
    func = parseCompile(input("\nEnter Function : "))
    n = int(input("\nEnter number of points n : "))
    gaussianQuadrature(a, b, n, func)
