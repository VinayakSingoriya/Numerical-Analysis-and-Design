
def readEqn(n):
    arr = list()
    for i in range(n):
        x = list(map(float, input().split()))
        arr.append(x)
    return arr


def printMatrix(a, n):
    for i in range(0, n):
        for j in range(0, n+1):
            print(a[i][j], end=" ")
        print()


def isvalid(a, n):
    valid = True
    for i in range(n):
        if (abs(a[i][i]) >= findSum(i, a)):
            continue
        else:
            valid = False
            break
    return valid


def findSum(row, a):
    sum = 0
    for i in range(n):
        if not(i == row):
            sum += abs(a[row][i])
        else:
            continue
    return sum


def jacobi(a, e, maxIt, n):
    if not(isvalid(a, n)):
        print(f">> Given System of Equation is not Diagonally Row Dominant.")
        exit()

    old_x = [0]*n
    new_x = [0]*n
    for k in range(0, maxIt):
        big_error = 0
        for i in range(0, n):
            sum = 0.0
            for j in range(0, n):
                if(i != j):
                    sum += a[i][j]*old_x[j]
            new_x[i] = (a[i][n]-sum)/a[i][i]

            E = abs((new_x[i]-old_x[i])/new_x[i])

            if E > big_error:
                big_error = E
            rel_error = big_error

        print(f"{k+1}=> {new_x} and Relative error:{rel_error}")
        if rel_error <= e:
            print(f"Solution is convergent.It converges in {k} iterations")
            return new_x

        for i in range(n):
            old_x[i] = new_x[i]

    print(f"Solution is not convergent at the {maxIt} iteration")

    return new_x


if __name__ == "__main__":
    n = int(input("Enter number of equations : "))
    arr = readEqn(n)
    print("----------------")
    printMatrix(arr, n)
    e = float(input("Enter Error : "))
    maxIt = int(input("Enter Max Iteration : "))
    values = jacobi(arr, e, maxIt, n)
    print("Values are :")
    for i in range(n):
        print(f"x[{i+1}] = {format(values[i], '.4f')}")
