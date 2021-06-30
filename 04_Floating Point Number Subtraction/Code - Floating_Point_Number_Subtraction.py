if __name__ == "__main__":
    print("\nFirst Floating Number format : x * 10^e, where 0.1 <= x < 1")
    print("\n>For Minuend : ")
    x1 = float(input("\tEnter mantissa x1 : "))
    e1 = int(input("\tEnter exponent e1 : "))

    print(">For Subtrahend : ")
    x2 = float(input("\tEnter mantissa x2 : "))
    e2 = int(input("\tEnter exponent e2 : "))

    k = abs(e1 - e2)
    if (e1 > e2):
        x2 = x2/pow(10, k)
        e = e1
    else:
        x1 = x1 / pow(10, k)
        e = e2 

    x = x1 - x2
    while( (abs(x) < 0.1) and (abs(x) > 0.0)):
        x = x*10
        e = e-1

    # Take mantissa upto 4 decimal degit
    x = format(x, ".4f")    

    if (e < -99):
        print("\n>> UNDERFLOW")
    print(f">> Result : {x} E{e}")              