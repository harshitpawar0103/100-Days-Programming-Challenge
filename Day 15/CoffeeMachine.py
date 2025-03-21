from CoffeeMachineDictionary import MENU, resources
menu = MENU

def turn_on():
    print("Turning on the machine ! ")
    c='y'
    while c=='y':
        choice = user_input()
        if check_resource1(choice):
            if process_coins(choice):
                make_coffee(choice)
        else :
            break
        c = input("wanna make coffe again ? : ")
    turn_off()
            
        

def turn_off():
    print("Turning off the machine ! ")

def report():
    print(f"water : {resources['water']}\nmilk : {resources['milk']}\ncoffee : {resources['coffee']}")

def check_resource(choice): # Mine
    if resources['water'] < menu[choice]["ingredients"]["water"]:
        print("water is insufficient")
        s = 0
    else :
        print("water is sufficient")
        s = 1
    if choice != "espresso" :
        if resources['milk'] < menu[choice]["ingredients"]["milk"]:
            print("milk is insufficient")
            s = 0
        else :
            print("milk is sufficient")
            s = 1
    if resources['coffee'] < menu[choice]["ingredients"]["coffee"]:
        print("coffee is insufficient")
        s = 0
    else :
        print("coffee is sufficient")
        s = 1
    if s == 1:
        print("Sufficient Ingredients")
    else : 
        print("Insufficient Ingredients")
    return s

def check_resource1(choice):  # ChatGPT
    insufficient_items = []
    
    # Ingredients required for the chosen drink
    ingredients = menu[choice]["ingredients"]
     
    # Check each required ingredient
    for item, required_amount in ingredients.items():
        if resources[item] < required_amount:
            insufficient_items.append(item)
    
    # Output results
    if insufficient_items:
        print(f"Insufficient Ingredients: {', '.join(insufficient_items)}")
        return 0  # Indicating insufficient resources
    else:
        print("Sufficient Ingredients")
        return 1  # Indicating sufficient resources

def process_coins(choice):
    q = int(input("How many quarters ? :"))
    d = int(input("How many dimes ? :"))
    n = int(input("How many nickles ? :"))
    p = int(input("How many pennies ? :"))
    t = q*0.25 + d*0.10 + n*0.05 + p*0.01
    r = t-menu[choice]['cost']
    if t >= menu[choice]['cost']:
        print("transaction successful ! You coffee is in making")
        print(f"Money returned after deduction : {r} $")
        return 1
    else : 
        print("insufficient money !")
        return 0


def make_coffee(choice):
    print(f"Here's your {choice} ! ")
    deduct_resources(choice)

def user_input():
    choice = input("What would you like ? (espresso,latte,cappucino) : ")
    return choice

def deduct_resources(choice):
    for item, required_amnt in menu[choice]["ingredients"].items():
        resources[item] -= required_amnt

        

turn_on()
report()
