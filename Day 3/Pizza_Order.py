print("Welocome to Python Pizza dileveries !")
size = input("What size pizza do you want ? M, L or S : ")
extra_cheese  = input("Do you want extra cheese ? Y or N : ").upper()
pepperoni = input("Do you want pepperpni on your pizza ? Y or N : ").upper()

bill = 0 
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else : 
    print("wrong input")

if size =="S" and pepperoni == "Y":
    bill += 2
elif size != "S" and pepperoni == "Y":
    bill += 3

if extra_cheese == "Y":
    bill += 1


print(f"Your Bill : $ {bill}")
