import time

def gameover():
    print('''
    
          .-.                     .-.               
          |U|                     | |               
          | |                     | |               
          | |                     | |               
         _| |_                   _| |_              
        | | | |-.               | |_| |-.           
       /|     ` |              / )| |_|_|           
      | |       |             | |-' `-^-'           
      |         |             |     ||  |           
      \         /             \     '   /           
       |       |               |       |            
       |       |               |       |            ''')
    exit()

def rightchoice():
    print("You chose the right way")


print('''


*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/____/___
*******************************************************************************
''')

print("Welcome to Treasure Island. way to find the treasure you want the most. Are you ready to polish your fortune ? \n\n ") 
input("Press enter  to start !!\n\n")

for i in range(5,0,-1):
    print(i,end = "\r")
    time.sleep(1)

print("Go")

if input("You have a crossroad in front of you. choose which is the blessed way \"left\" or \"right\" : ").lower() == "right":
    print("You fell in a pit.")
    gameover()

rightchoice()

if input("Now there is a lake in your way to the island. Do you want to swim across(type \"swim\") or wait (\"wait\") for the boat ? : ").lower() == 'swim':
    print("You're dead. you became feast of crocodiles.")
    gameover()

rightchoice()

if input('''You arrived at the island unharmed.
There is a cave with three doors :
Red 
Blue
Yellow
            
which colour gate you wanna enter : ''').lower() == "red":
    print("\n\nYou found the chest full of gold coins")

    

