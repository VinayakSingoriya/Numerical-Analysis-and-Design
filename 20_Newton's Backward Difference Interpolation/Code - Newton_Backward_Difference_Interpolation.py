
def read():
    print("Enter x values : ", end="")
    x = list(map(float, input().split()))
    print("Enter f(x) values : ", end="")
    y = list(map(float, input().split()))
    return x, y


def difference(y, n):
    d = [[0]*(n-1) for i in range(n-1)]
    for j in range(n-1):
        for i in range(n-j-1):
            if (j == 0):
                d[i][j] = y[i+1] - y[i]
            else:
                d[i][j] = d[i+1][j-1] - d[i][j-1]
    # print(d)
    return d


def num(u, i):
    mul = 1
    for j in range(i+1):
        mul *= u+j
    return mul


def fac(n):
    return 1 if (n == 1 or n == 0) else n * fac(n - 1)


def NBDIF(x_arr, y_arr, x, n):
    h = x_arr[1] - x_arr[0]
    u = (x-x_arr[n-1]) / h
    d = difference(y_arr, n)
    result = y_arr[n-1]
    for i in range(n-1):
        result += (num(u, i)/fac(i+1))*d[n-2-i][i]
        print(result)
    print(f"\n>> f({x}) = {result}")


if __name__ == "__main__":
    n = int(input("Enter number of elements : "))
    x_arr, y_arr = read()
    continue_ = 'y'

    while(continue_ == 'y'):
        x = float(input("Enter x : "))
        # if not(x_arr[0] <= x <= x_arr[n-1]):
        #     print(f"\n>>Given x value lies outside tabulated range.")
        #     exit()
        result = NBDIF(x_arr, y_arr, x, n)
        continue_ = input(
            "\nDo you want to compute again for the same table?(y/n) : ")
