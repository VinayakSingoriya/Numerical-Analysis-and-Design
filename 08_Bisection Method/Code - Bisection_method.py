# Bisection Method : In mathematics, the bisection method is a root-finding method that applies to any continuous functions for which one knows two values with opposite signs.
def eqn(x):
    return x*x - x - 1

def bisection(a,b,E):
    if (eqn(a)*eqn(b)) > 0:
        print(f"\n>>Roots are not in the given interval [{a},{b}]")
        exit()

    else:
        i = 1
        m = (a+b)/2
        print("-----------------------------------------------------------------------------------------")
        print("i\t|\t  a\t|\t  b\t|\t  m\t|\t  f(m)\t|    f(a)*f(m)  |")
        print("-----------------------------------------------------------------------------------------")
        while(abs(eqn(m))>E):
            print(f"{i}\t|\t{format(a, '.4f')}\t|\t{format(b, '.4f')}\t|\t{format(m, '.4f')}\t|\t{format(eqn(m), '.4f')}\t|\t{format(eqn(a)*eqn(m), '.4f')}\t|")
            if eqn(a)*eqn(m) > 0:
                a = m
            else:
                b = m
            m = (a+b)/2  
            i+=1      

        print(f"{i}\t|\t{format(a, '.4f')}\t|\t{format(b, '.4f')}\t|\t{format(m, '.4f')}\t|\t{format(eqn(m), '.4f')}\t|\t{format(eqn(a)*eqn(m), '.4f')}\t|")
        print("-----------------------------------------------------------------------------------------")
        
        print(f"\n>>Roots : {format(m, '.4f')}")

          
if __name__ == "__main__":
    a = float(input("Enter value of a : "))
    b = float(input("Enter value of b : "))
    E = 0.0001
    bisection(a,b,E)
 

            
            




    