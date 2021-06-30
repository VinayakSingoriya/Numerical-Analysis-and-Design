# Code to implement Horner's Method for the evaluation of polynomial of n degree
#Horner's Method allows the evaluation of polynomial of n degree with only n multiplications and n additions.
# Time complexity : O(n)

def hornerMethod(poly, x, degree):
    result = poly[0]
    for i in range(1, degree+1):
        result = poly[i] + x*result
    return result    


if __name__ == "__main__":
    degree = int(input("Enter Degree of polynomial: "))
    print("Enter corfficients in the decreasing power of x (space separated input): ")
    poly = list(map(float, input().split()))
    x = float(input("Enter x : "))  
    print("\nValue is : ", hornerMethod(poly, x, degree))