def read():
    print("Enter x values : ", end="")
    x = list(map(float, input().split()))
    print("Enter y values : ", end="")
    y = list(map(float, input().split()))
    return x,y  

def d_difference(x, y, n):
    d = [[0]*(n-1) for i in range(n-1)]
    for j in range(n-1):
        for i in range(n-j-1):
            if (j==0):
                d[i][j] = (y[i+1]-y[i])/(x[i+1]-x[i])
            else:
                d[i][j] = (d[i+1][j-1]-d[i][j-1])/(x[i+j+1]-x[i])
    return d                


def printTable(d, n):
    print("\n\t----------------------------------------------")  
    for i in range(1, n):
        print(f"\t| ⍋{[i]} ", end="")  
    print("\n\t----------------------------------------------")  

    for i in range(n-1):
        
        for j in range(n-1-i):
            print(f"\t  {format(d[i][j], '.2f')}", end="")
        print()                      
    print("\n\t----------------------------------------------")  



if __name__ == "__main__":
    n = int(input("Enter number of elements : "))
    x, y = read()
    d = d_difference(x,y,n)
    print("\nDivided DIFFERENCE TABLE :")
    printTable(d, n)



    
