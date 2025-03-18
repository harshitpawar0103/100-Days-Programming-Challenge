import random as r

check = input("do you wanna play blackjack ? y or n : ")
while check == 'y':
    print("\0337",end="")
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,"Ace"]
    player = [r.choice(cards),r.choice(cards)]
    player_score = computer_score = 0
    c='y'
    result = 1
    computer = [r.choice(cards),r.choice(cards)]
    if "Ace" in computer:
            s = r.choice([1,11])
            for i in range(len(computer)):
                if computer[i] == "Ace":
                    computer[i] = s
    computer_score = sum(computer)
    while (player_score <=21 ) and c=='y':
        if "Ace" in player:
            s = int(input("Choose your lucky number 1 or 11 :"))
            for i in range(len(player)):
                if player[i] == "Ace":
                    player[i] = s
        player_score = sum(player)
        print(f"Your cards : {player}, current score : {player_score}")
        print(f"Computer's first card : {computer[0]}")
        if player_score > 21:
            print("You lost")
            result = 0
            break
        c = input("Type 'y' to get another card, type 'n' to pass : ")
        if c=='y':
            player.append(r.choice(cards))
        
    if result == 1:
        while computer_score <= 21 and computer_score < player_score :
            computer.append(r.choice(cards))
            if "Ace" in computer:
                if computer_score <= 10:
                    s = 11
                else :
                    s = 1
                for i in range(len(computer)):
                    if computer[i] == "Ace":
                        computer[i] = s
            computer_score = sum(computer)
        

    print(f"Your final hand : {player}, final score : {player_score}")
    print(f"Computer's final hand : {computer}, final score : {computer_score}")
    
    if result == 1 :
        if computer_score > 21:
            print("You win")
        elif player_score > computer_score:
            print("You win")
        elif player_score == computer_score:
            print("tie")
        else : 
            print("You lost")
    check = input("do you wanna play blackjack ? y or n : ")