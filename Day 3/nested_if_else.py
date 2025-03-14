# if condition:
#     if another_condition:
#         do this
#     else :
#         do this
# else :
#     do this 

print("Welcome to the rollercoster ride")
height = int(input("Enter your height (in cm) : "))

if height >= 120 :
    age = int(input("Enter your age : "))
    if age >= 18 :
        print("Pay $12 ticket price")
    else :
        print("Pay $7 ticket price")

else : 
    print("Not Allowed")
