import random as r
print(''' 
$$$$$$\                                                  $$\     $$\                                                         $$\                           
$$  __$$\                                                 $$ |    $$ |                                                        $$ |                          
$$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\       $$$$$$\   $$$$$$$\   $$$$$$\        $$$$$$$\  $$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|      \_$$  _|  $$  __$$\ $$  __$$\       $$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\          $$ |    $$ |  $$ |$$$$$$$$ |      $$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\         $$ |$$\ $$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |        \$$$$  |$$ |  $$ |\$$$$$$$\       $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \______/  \______/  \_______|\_______/ \_______/          \____/ \__|  \__| \_______|      \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|   ''')



print("\n\n\nWelcome to the number guessing game.")
print("I'm thinking of a number between 1 and 100")
diff = input("Choose a difficulty level. Type 'easy' or 'hard'  : " )
if diff == "easy":
    n = 9
elif diff =="hard":
    n = 5
else :
    print("wrong input")

num = r.randint(1,100)

while n>0:
    print(f"You have {n} attempts remaining to guess a number.")
    guess = int(input("Make a guess : "))
    if guess < num :
        print("Too low")
    elif guess > num:
        print("Too High")
    elif guess == num:
        print(f"You got it. The answer is {guess}")
        break
    else :
        pass
    n=n-1

