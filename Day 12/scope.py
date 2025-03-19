enemies = 1 

def increase_enemies():
    enemies = 2
    print(f"Inside function : {enemies}") # prints enemies = 2 defined within the function 

increase_enemies()
print(f"Outside function : {enemies}") # prints enemies = 1 defined in global scope 


# Local scope 

def drink_potion():
    potion_strength = 4
    print(potion_strength)

drink_potion()
# print(potion_strength) # It'll give error


# global Scope 
player_health = 6
def drink_potion():
    potion_strength = 4
    print(player_health)
