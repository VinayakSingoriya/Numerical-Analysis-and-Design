
def read():
    print("Enter x values : ", end="")
    x = list(map(float, input().split()))
    print("Enter f(x) values : ", end="")
    y = list(map(float, input().split()))
    return x, y


def num(x, i, x_arr):
    mul = 1
    for j in range(n):
        if(j != i):
            mul *= x - x_arr[j]
    return mul


def deno(i, x_arr):
    mul = 1
    for j in range(n):
        if (j != i):
            mul *= x_arr[i] - x_arr[j]
    return mul


def Legrange_Iterpolation(x_arr, y_arr, x, n):
    result = 0
    for i in range(n):
        result += (num(x, i, x_arr)/deno(i, x_arr))*y_arr[i]
        print(result)
    print(f"\n>> f({x}) = {result}")


if __name__ == "__main__":
    n = int(input("Enter number of elements : "))
    x_arr, y_arr = read()
    continue_ = 'y'

    while(continue_ == 'y'):
        x = float(input("Enter x : "))
        result = Legrange_Iterpolation(x_arr, y_arr, x, n)
        continue_ = input(
            "\nDo you want to compute again for the same table?(y/n) : ")
