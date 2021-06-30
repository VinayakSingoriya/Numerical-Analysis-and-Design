# Time Complexity of Gauss-Jordan Method : O(n)

def readEqn(n):
    arr = list()
    for i in range(n):
        x = list(map(float, input().split()))
        arr.append(x)
    return arr

 # This function will convert given augmented matrix into upper traingular


def diagonalMatrix(a, n):
    for k in range(0, n):
        i_max = k
        v_max = a[i_max][k]
        for i in range(k+1, n):
            if (abs(a[i][k]) > v_max):
                v_max = a[i][k]
                i_max = i

        if not(a[k][i_max]):
            if (k != -1):
                print("Singular matrix")
            if (a[k][n]):
                print("Inconsistent System.")
            else:
                print("May have infinitely many solutions.")
            exit()

        if (i_max != k):
            a = swap_row(a, k, i_max, n)

        for i in range(0, n):
            u = a[i][k]/a[k][k]
            if(i != k):
                for j in range(k, n+1):  # apply row transformation on every element of row
                    a[i][j] = a[i][j]-(a[k][j]*u)
    return a


def swap_row(a, i, j, n):
    for k in range(n+1):
        temp = a[i][k]
        a[i][k] = a[j][k]
        a[j][k] = temp
    return a


def values(a, n):
    x = [0]*n
    for i in range(0, n):
        x[i] = a[i][n]/a[i][i]
    return x


if __name__ == "__main__":
    n = int(input("Enter number of equations : "))
    arr = readEqn(n)
    dArray = diagonalMatrix(arr, n)
    print(dArray)
    values = values(dArray, n)
    print("Answer : ")
    for value in values:
        print(format(value, '.4f'))
