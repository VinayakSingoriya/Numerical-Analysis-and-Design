#Simpson's 1/3 Rule to compute the difinite integral of a function(in tabular form).
# Input required for this code is : Tabular Form


def read():
    print("Enter x values : ", end="")
    x = list(map(float, input().split()))
    print("Enter f(x) values : ", end="")
    y = list(map(float, input().split()))
    return x, y


def simpsonOneThird(x_arr, y_arr, n):
    h = x_arr[1]-x_arr[0]
    sum = y_arr[0]+y_arr[n-1]
    for i in range(1, n-1):
        if (i%2==0):
            sum += 2*y_arr[i]
        else:
            sum += 4*y_arr[i]

    integral = (sum*h)/3
    print(f'\n>> Intergral = {integral}\n')        




if __name__ == "__main__":
    n = int(input("Enter number of known co-ordinate n : "))
    x_arr, y_arr = read()
    simpsonOneThird(x_arr, y_arr, n)
