import random as r
def stone():
    print('''
         _.-._                     
        | | | |-. 
       /|     ` |                
      | |       |                
      |         |                
      \         /    
       |       |     
       |       |            
''')

def paper():
    print('''
          .-.              
        .-|U|-.         
        |U| |U|        
        | | | |-.      
        | | | |U|
        | | | | |      
       /|     ` |     
      | |       |    
      |         |
      \         /    
       |       |
       |       | 
''')

def scissor():
    print('''            
      (>\       _    
     (>\ \     /<)  
      \ \ \   / /    
       \ \ \ / /<)    
        \ \ V / /      
       /| '   ` |     
      | |       |    
      |         |    
      \         /    
       |       |      
       |       | ''')

print('''Wanna play Stone Paper Scissor ? 
Choose :
1 - Stone
2 - Paper 
3 - Scissor''')

p_choice = int(input("Enter your choice : "))

if p_choice not in [1,2,3]: 
    print("wrong choice")
    exit()

c_choice = r.randint(1,3)
if p_choice == 1:
    stone()
elif p_choice == 2:
    paper()
elif p_choice == 3:
    scissor()

if c_choice == 1:
    print("Computer chose Stone : \n\n")
    stone()
elif c_choice == 2:
    print("Computer chose Paper : \n\n")
    paper()
elif c_choice == 3:
    print("Computer chose Scissor : \n\n")
    scissor()
if p_choice == c_choice :
    print("it's a tie.")
else :
    if p_choice == 1 and c_choice == 2 :
        print("computer won")
    elif p_choice == 1 and c_choice == 3 :
        print("You won")
    elif p_choice == 2 and c_choice == 1 :
        print("You won")
    elif p_choice == 2 and c_choice == 3 :
        print("computer won")
    elif p_choice == 3 and c_choice == 1 :
        print("computer won")
    elif p_choice == 3 and c_choice == 2 :
        print("You won")

    