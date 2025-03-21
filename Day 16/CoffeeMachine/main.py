from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m1 = Menu()
print(m1.get_items())
choice = input("What would you like ? (espresso,latte,cappucino) : ")
item = m1.find_drink(choice)
print(item)
c1 = CoffeeMaker()
m1 = MoneyMachine()
if c1.is_resource_sufficient(item):
    if m1.make_payment(item.cost):
        c1.make_coffee(item)
    
