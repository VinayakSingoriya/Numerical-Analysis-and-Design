import sympy as sym
def diff(expression):
    x = sym.Symbol('x')
    return(str(sym.diff(expression)))


def eqn(x, equation):
    return eval(equation)

def Newton(b, E, e):
    E1 = diff(E)
    m = b - (eqn(b, E)/eqn(b, E1))
    i = 1
    print("---------------------------------------------------------")
    print("i\t|\t  b\t|\t  m\t|\t  f(m)\t|")
    print("---------------------------------------------------------")
    while(abs(eqn(m, E))>0):
        print(f"{i}\t|\t{format(b, '.4f')}\t|\t{format(m, '.4f')}\t|\t{format(eqn(m, E), '.4f')}\t|")
        b = m
        m = b - (eqn(b, E)/eqn(b, E1))
        i+=1
    print(f"{i}\t|\t{format(b, '.4f')}\t|\t{format(m, '.4f')}\t|\t{format(eqn(m, E), '.4f')}\t|")
    print("---------------------------------------------------------")
    print(f"\n>>Root : {format(m, '.4f')}")

if __name__ == "__main__":
    b = float(input("Enter initial Guess value : "))
    e = 0.0001
    E = "x*x-25"
    Newton(b, E, e)
        





