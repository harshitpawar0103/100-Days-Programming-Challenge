while 1!=0:
    print("\033c", end="")
    n1 = int(input("What's the first number ? :"))
    check = 'y'
    while check == 'y':
        print("+\n-\n*\n/")
        o = input("Pick an operation : ")
        n2 = int(input("What's the next number ? : "))
        if o=="+":
            s=n1+n2
            print(f"{n1} + {n2} = {s}")
        elif o=="-":
            s=n1-n2
            print(f"{n1} - {n2} = {s}")
        elif o=="*":
            s=n1*n2
            print(f"{n1} * {n2} = {s}")
        elif o=="/":
            s=n1/n2
            print(f"{n1} / {n2} = {s}")
        else : 
            s=0.0
            print(f"{n1} undefined {n2} = {s}")

        check = input(f"Type 'y' to continue calculating with {s}, or type 'n'to start a new calculation : ")
        n1 = s
