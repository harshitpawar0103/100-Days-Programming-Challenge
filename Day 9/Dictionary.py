programming_dict = {
    "Variable": "A named storage for data that can be changed during program execution.",
    "Function": "A reusable block of code that performs a specific task when called.",
    "Loop": "A structure that repeats a block of code multiple times (e.g., for, while loops).",
    "Conditional": "A statement that executes different code based on conditions (e.g., if-else).",
    "List": "An ordered, mutable collection of elements in Python.",
    "Dictionary": "A collection of key-value pairs, allowing fast lookups.",
    "Recursion": "A function calling itself to solve a problem in smaller subproblems.",
    "OOP": "Object-Oriented Programming, a paradigm based on classes and objects.",
    "API": "Application Programming Interface, a way for programs to communicate with each other.",
    "Exception": "An error that occurs during execution, which can be handled using try-except blocks."
}

# print(programming_dict["OOP"])
# print(programming_dict)


# wipe an existing dictionary
# programming_dict = {}
# print(programming_dict)


# Edit an item from the dictionary
programming_dict["Loop"] = "circle rope on your computer"

# print(programming_dict["loop"] )



# Loop through a dictionary
for key in programming_dict:
    print(key)
    print(programming_dict[key])