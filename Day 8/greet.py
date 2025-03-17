name = input("Enter your name : ")
def greet():
    print(f"Hello {name} ! How are you ?")

greet()

# function with parameter 
print("\n\n\n")
def greet(Name):
    print(f"Hello {Name}! How are you ?")

greet("Arya")

# Here Name is parameter and "Arya" is an argument


# functions in positional arguments

def name_and_loc(name,location):
    print(f"\nHello {name}\nWhat's in like {location} ?")

name_and_loc("Naman","IIT Bombay")

# change in order of positional arguments gives error
name_and_loc("IIT Bombay","Naman")

# do it right with keyword arguments
name_and_loc(location = "IIT Indore",name = "Naman")


# functions with keyword argument
def my_function(a,b,c):
    print(f"\na = {a}\nb = {b}\nc = {c}")

my_function(c=3,b=2,a=1)

