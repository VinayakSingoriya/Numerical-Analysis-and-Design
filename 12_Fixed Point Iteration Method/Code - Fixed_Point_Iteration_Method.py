
def eqn(x, equation):
    return eval(equation)


def Fixed_Iteration(b, f, f1, E):
    i = 1
    m = eqn(b, f1)
    print("\n----------------------------------------------------------")
    print("i\t|\t  b\t|\t  m\t|\tabs(b-m) |")
    print("\n----------------------------------------------------------")
    while(abs(b-m) > E):
        print(
            f"{i}\t|\t{format(b, '.4f')}\t|\t{format(m, '.4f')}\t|\t{format(abs(b-m), '.4f')}   |")
        b = m
        m = eqn(b, f1)
        i += 1

    print(f"{i}\t|\t{format(b, '.4f')}\t|\t{format(m, '.4f')}\t|\t{format(abs(b-m), '.4f')}   |")

    print("\n----------------------------------------------------------")

    print(f"\n>> Roots : {format(m, '.4f')}\n")


if __name__ == "__main__":
    b = float(input("Enter initial Guess Value b : "))
    E = 0.0001
    f = "x*x-x-1"
    f1 = "(x+1)**0.5"
    Fixed_Iteration(b, f, f1, E)
