import random as r
friends = ["Tommen","Theon","Jon Snow","Sam","Stannis","Melisandre","Margeary"]



# option 1
n = r.randint(0,6)
print(f"{friends[n]} will pay the bill.")


# option 2
print(f"{r.choice(friends)}  will pay the bill.")