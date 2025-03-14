print("Welcome to the rollercoster ride")
height = int(input("Enter your height (in cm) : "))

if height >= 120 :
    age = int(input("Enter your age : "))
    if age <= 12:
        bill = 5
        print("Pay $5 ticket price")
    elif age < 18:
        bill = 7
        print("Pay $7 ticket price")
    elif age < 45 : 
        bill = 12
        print("Pay $12 ticket price")
    elif age >=45 and age <=55:
        print("free ride")
    want_photo = input("Do you want to click photo ? Y or N : ")
    if want_photo=="Y":
        bill += 3
        print("Pay extra $3")
    print(f"Total Bill :  $ {bill}")

else : 
    print("Not Allowed")
