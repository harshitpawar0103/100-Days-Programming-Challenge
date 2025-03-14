# print(len(12345)) - gives type error

# Subscripting 
print("Hello"[0]) # prints H
print("Hello"[-1])  # prints o

# Data Types 

# Strings

print("123" + "345") # prints 123345

# Integer = Whole Number

print(123 + 456) # prints 579

# Large Integers
print(123_456_563) # prints 123456563

#Float = floating point numbers
print(3.14159)

# Boolean
print(True)
print(False)

# len(12345) TypeError: object of type 'int' has no len()

# to know the data type
print(type("Hello"))
print(type(3.1459))
print(type(456))
print(type(True))


# Type Conversion
print(int("123") + int("456")) # print 579
#print(int("abc") + int("456")) # ValueError: invalid literal for int() with base 10: 'abc'

print(f"Number of letters in your name : {len(input('Enter your name : '))}" )




