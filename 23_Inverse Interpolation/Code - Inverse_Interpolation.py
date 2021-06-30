
def read():
    print("Enter x values : ", end="")
    x = list(map(float, input().split()))
    print("Enter f(x) values : ", end="")
    y = list(map(float, input().split()))
    return x, y


def num(y, i, y_arr):
    mul = 1
    for j in range(n):
        if(j != i):
            mul *= y - y_arr[j]
    return mul


def deno(i, y_arr):
    mul = 1
    for j in range(n):
        if (j != i):
            mul *= y_arr[i] - y_arr[j]
    return mul


def Inverse_Iterpolation(x_arr, y_arr, y, n):
    result = 0
    for i in range(n):
        result += (num(y, i, y_arr)/deno(i, y_arr))*x_arr[i]
    print(f"\n>> x = {result}")


if __name__ == "__main__":
    n = int(input("Enter number of elements : "))
    x_arr, y_arr = read()
    continue_ = 'y'

    while(continue_ == 'y'):
        y = float(input("Enter y : "))
        result = Inverse_Iterpolation(x_arr, y_arr, y, n)
        continue_ = input(
            "\nDo you want to compute again for the same table?(y/n) : ")
