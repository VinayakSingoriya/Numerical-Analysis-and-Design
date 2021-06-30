import math
if __name__ == "__main__":
    a = float(input('Enter value of a : '))
    b = float(input("\nEnter value of b : "))
    c = float(input("\nEnter value of c : "))

    if(a==0):
        print("\n>> Given equation is not a quadratic equation.")
        if(b!=0):
            x = -(c/b)
            print(f"\nx ={x}")
        else:
            print("\n>> The Given equation is not a valid equation.")
    else:
        D = (b*b) - (4*a*c)
        if(D==0):
            print("\nRoots are Real and Equal.")
            alpha = beta = -(b/(2*a))
        elif(D>0):
            print("\nRoots are Real and Distinct.")
            alpha = (-b + math.sqrt(D))/ (2*a)   
            beta = (-b - math.sqrt(D))/ (2*a)
        else:
            print("\n>> Roots are Imaginary / Complex.")
            x_real = -b/(2*a)
            x_imaginary = math.sqrt(abs(D)) / (2*a)
            alpha = f"{x_real} + i {x_imaginary}"
            beta = f"{x_real} - i {x_imaginary}"
        print('\nFirst Root :',alpha)  
        print("\nSecond Root :",beta)     
