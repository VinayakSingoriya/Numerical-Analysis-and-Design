if __name__ == "__main__":
    print("\nFirst Floating Number format : x * 10^e, where 0.1 <= x < 1")
    print(">For First Number : ")
    x1 = float(input("\tEnter mantissa x1 : "))
    e1 = int(input("\tEnter exponent e1 : "))

    print(">For Second Number : ")
    x2 = float(input("\tEnter mantissa x2 : "))
    e2 = int(input("\tEnter exponent e2 : "))

    x = x1 * x2
    e = e1 + e2

    if (abs(x) >= 1.0):
        x = x / 10
        e = e + 1

    if (abs(x) < 0.1):
        x = x * 10
        e = e - 1    

    if (e > 99):
        print("\n>> OVERFLOW")    
    elif (e < -99):
        print("\n>> UNDERFLOW")

    # print(f"Result : {format(x, '.4f')} E{e}")   
    print(f"Result : {x} E{e}")   

