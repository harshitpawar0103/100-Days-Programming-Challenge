print("Welcome to the tip calculator")
bill = float(input("What was the total bill ? $"))
tip = int(input("How percent tip would you like to give ? 10,12 or 15 : "))
person = int(input("How many people to split the bill ? "))

per_person_share = round((bill + bill*(tip/100))/person,2)

print(f"Each person should pay : $ {per_person_share}")