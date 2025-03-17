import random as r
from hangman_words import hn_words
from hangman_draw import logo,stages
print("Welcome to Hangman Game. Let's test your vocabulary !")

print(logo)

# Set lives 
lives = 6

# wtbg - word to be guessed
wtbg = r.choice(hn_words)

# wtbg_list - convert wtbg into list of apphabets
wtbg_list = list(wtbg)

# u_wtbg_list - set of unique alphabets in wtbg_list
u_wtbg_list = list(set(wtbg_list))

# Initialize the letter_guessed_list with no alphabets
letter_guessed_list = []

while lives > 0 and len(letter_guessed_list)<=len(u_wtbg_list):
    print("\nWord to Guess : ",end="")

    # print blanks and rightly guessed letters
    for i in range(len(wtbg)):
        if wtbg_list[i] in letter_guessed_list:
            print(wtbg_list[i],end="")
        else :
            print("_",end= "")

    # Input the Letter
    letter_guessed = input("\nGuess a letter : ")
    if len(letter_guessed)>1:
        print("You entered more than one letter. You lost a life. Kindly enter single alphabet next time.")
        lives-=1
        print(stages[lives])
        continue


    if letter_guessed in wtbg_list:
        print("Your guess is right")
        letter_guessed_list.append(letter_guessed)
    else : 
        print(f"You guessed {letter_guessed}, that's not in the word. You lost a life.")
        lives-=1
        print(stages[lives])


    if len(letter_guessed_list)==len(u_wtbg_list):
        print("You won the game.") 
        break
    

if lives == 0:
    print("You lost")
    print(f"The word was : {wtbg}")