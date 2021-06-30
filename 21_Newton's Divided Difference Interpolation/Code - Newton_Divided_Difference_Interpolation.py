
def read():
    print("Enter x values : ", end="")
    x = list(map(float, input().split()))
    print("Enter f(x) values : ", end="")
    y = list(map(float, input().split()))
    return x, y


def d_difference(x, y, n):
    d = [[0]*(n-1) for i in range(n-1)]
    for j in range(n-1):
        for i in range(n-j-1):
            if (j == 0):
                d[i][j] = (y[i+1]-y[i])/(x[i+1]-x[i])
            else:
                d[i][j] = (d[i+1][j-1]-d[i][j-1])/(x[i+j+1]-x[i])
    return d


def term(x, x_arr, i):
    mul = 1
    for j in range(i+1):
        mul *= x - x_arr[j]
    return mul


def NDDIF(x_arr, y_arr, x, n):
    d = d_difference(x_arr, y_arr, n)
    result = y_arr[0]
    for i in range(n-1):
        result += term(x, x_arr, i)*d[0][i]
    print(f"\n>> f({x}) = {result}")


if __name__ == "__main__":
    n = int(input("Enter number of elements : "))
    x_arr, y_arr = read()
    continue_ = 'y'

    while(continue_ == 'y'):
        x = float(input("Enter x : "))
        result = NDDIF(x_arr, y_arr, x, n)
        continue_ = input(
            "\nDo you want to compute again for the same table?(y/n) : ")
