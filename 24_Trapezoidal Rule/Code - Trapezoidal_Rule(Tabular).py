# Trapezoidal rule to compute definite integral of a function(in tabular form)
# Input required : Tabular Form

def read():
    print("Enter x values : ", end="")
    x = list(map(float, input().split()))
    print("Enter f(x) values : ", end="")
    y = list(map(float, input().split()))
    return x, y


def Trapezoidal(x_arr, y_arr, n):
    h = x_arr[1] - x_arr[0]
    sum = y_arr[0] + y_arr[n-1]

    for i in range(1, n-1):
        sum += 2*y_arr[i]
    integral = (sum*h)/2
    print(f'\n>> Intergral = {integral}\n')


if __name__ == "__main__":
    n = int(input("Enter number of known co-ordinate n : "))
    x_arr, y_arr = read()
    Trapezoidal(x_arr, y_arr, n)
