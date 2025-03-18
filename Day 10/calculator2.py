def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

def subtract(a,b):
    return a-b

def add(a,b):
    return a+b

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}

print(operations['+'](7,8))
while 1!=0:
    print("\033c",end="")
    n1 = int(input("What's the first number ? : "))
    check = 'y'
    while check == 'y':
        print("\n+\n-\n*\n/")
        o = input("What's the operation ? : ")
        n2 = int(input("What's the next number ? : "))
        if o in operations:
            s = operations[o](n1,n2)
            print(f"{n1} {o} {n2} = {s}")
        else :
            print(f"{n1} undefined {n2} = 0.0")
        check = input(f"Type 'y' to continue calculating with {s}, or type 'n'to start a new calculation : ")
        n1 = s
        
