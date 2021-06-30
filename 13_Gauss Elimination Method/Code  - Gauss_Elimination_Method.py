# Time Complexity of Gauss Elimination Method : O(n^3)

def readEqn(n):
    arr = list()
    for i in range(n):
        x = list(map(float, input().split()))
        arr.append(x)
    return arr

 # This function will convert given augmented matrix into upper traingular


def fwElimination(a, n):
    for k in range(0, n-1):  # For making Zero in (n-1)th row
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

        for i in range(k+1, n):  # Start making Zero from (n-1)th position for nth row
            u = a[i][k]/a[k][k]
            for j in range(k, n+1):  # apply row transformation on every element of row
                a[i][j] = a[i][j]-(a[k][j]*u)
    return a


def swap_row(a, i, j, n):
    for k in range(n+1):
        temp = a[i][k]
        a[i][k] = a[j][k]
        a[j][k] = temp
    return a


def bwSubstitution(a, n):
    x = [0]*(n)
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum = sum + a[i][j]*x[j]
        x[i] = (a[i][n]-sum)/a[i][i]
    return x


if __name__ == "__main__":
    n = int(input("Enter number of equations : "))
    arr = readEqn(n)
    eArray = fwElimination(arr, n)
    print(eArray)
    values = bwSubstitution(eArray, n)
    print("Answer : ")
    for value in values:
        print(format(value, '.4f'))
