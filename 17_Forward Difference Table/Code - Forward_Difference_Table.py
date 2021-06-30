def read():
    print("Enter y values : ", end="")
    y = list(map(float, input().split()))
    return y    

def f_difference(y, n):
    d = [[0]*(n-1) for i in range(n-1)]
    for j in range(n-1):
        for i in range(n-j-1):
            if (j == 0):
                d[i][j] = y[i+1] - y[i]
            else:
                d[i][j] = d[i+1][j-1] - d[i][j-1]
    # print(d)            
    return d 

def printTable(d, n):
    print("\n\t----------------------------------------------")  
    for i in range(1, n):
        print(f"\t| ∆{[i]} ", end="")  
    print("\n\t----------------------------------------------")  

    for i in range(n-1):
        
        for j in range(n-1-i):
            print(f"\t  {d[i][j]}", end="")
        print()                      
    print("\n\t----------------------------------------------")  



if __name__ == "__main__":
    n = int(input("Enter number of elements : "))
    y = read()
    d = f_difference(y, n)
    print("\nFORWARD DIFFERENCE TABLE :")
    printTable(d, n)


    
