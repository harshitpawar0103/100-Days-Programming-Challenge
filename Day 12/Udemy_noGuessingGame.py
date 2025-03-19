import random as r

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(g,n,t):
    if g==n:
        print(f"You guessed it right. The number is : {g}")
        exit()
    elif g>n:
        print("Too high")
    elif g<n:
        print("too Low")
    else : 
        pass
    t-=1
    print(f"You have {t} attempts remaining to guess a number")
    return t

def set_difficulty():
    level = input("Choose difficulty level. 'easy' or 'hard' : ")
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else :
        print("worng input")
        return 0
def game():
    print("Welcome to the no guessing game !")
    print("I'm thinking of a number between 1 and 100.")
    num = r.randint(1,100)

    turns = set_difficulty()

    while turns > 0:
        guess = int(input("Make a guess : "))
        turns = check_answer(guess,num,turns)
    
    print("You lost")

game()