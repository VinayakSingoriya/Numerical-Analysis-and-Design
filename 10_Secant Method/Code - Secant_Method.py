def eqn(x):
    return x*x - x - 1

def secant(a,b,E):
        i = 1
        m = (a*eqn(b) - b*eqn(a)) / (eqn(b) - eqn(a))
        print("-----------------------------------------------------------------------------------------")
        print("i\t|\t  a\t|\t  b\t|\t  m\t|\t  f(m)\t|    f(a)*f(m)  |")
        print("-----------------------------------------------------------------------------------------")
        while(abs(eqn(m))>E):
            print(f"{i}\t|\t{format(a, '.4f')}\t|\t{format(b, '.4f')}\t|\t{format(m, '.4f')}\t|\t{format(eqn(m), '.4f')}\t|\t{format(eqn(a)*eqn(m), '.4f')}\t|")
            a, b = b, m
            m = (a*eqn(b) - b*eqn(a)) / (eqn(b) - eqn(a)) 
            i+=1      

        print(f"{i}\t|\t{format(a, '.4f')}\t|\t{format(b, '.4f')}\t|\t{format(m, '.4f')}\t|\t{format(eqn(m), '.4f')}\t|\t{format(eqn(a)*eqn(m), '.4f')}\t|")
        print("-----------------------------------------------------------------------------------------")
        
        print(f"\n>>Roots : {format(m, '.4f')}")

          
if __name__ == "__main__":
    a = float(input("Enter value of a : "))
    b = float(input("Enter value of b : "))
    E = 0.0001
    secant(a,b,E)