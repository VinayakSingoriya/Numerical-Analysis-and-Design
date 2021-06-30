if __name__ == "__main__":
    print("First Equation format : ax + by = c")
    print("Second Equation format : px + qy = r")

    a = float(input("\nEnter value of a : ")) 
    b = float(input("\nEnter value of b : ")) 
    c = float(input("\nEnter value of c : "))
    p = float(input("\nEnter value of p : ")) 
    q = float(input("\nEnter value of q : ")) 
    r = float(input("\nEnter value of r : ")) 

    q = q - ((p*b)/a)
    r = r - ((p*c)/a)
    
    if (q==0):
        print("No Solution.")
        exit()
    y = r/q
    x = (c-(b*y))/a    

    print(f'\nx = {x}')
    print(f'\ny = {y}')

    