# This version of game remove used card in each instance of game when card is drawn by either by player or user
import random as r
def calculate_score(hand):
    score = sum(card if card!="Ace" else 11 for card in hand)
    for i in range(len(hand)):
        if score > 21 and hand[i] == "Ace":
            score-=10
    return score
    
def card_deck(hand,deck):
    for card in range(len(hand)):
        if hand[card] in deck:
            for i in range(len(deck)):
                if hand[card] == deck[i]:
                    deck.pop(i)
                    break
    return deck

def play_blackjack():
    check = input("do you wanna play blackjack ? y or n : ")
    p_cards = [2,3,4,5,6,7,8,9,10,10,10,10,"Ace"]
    c_cards = [2,3,4,5,6,7,8,9,10,10,10,10,"Ace"]
    while check == 'y':
        player = [r.choice(p_cards),r.choice(p_cards)]
        p_cards = card_deck(player,p_cards)
        
        comp = [r.choice(c_cards),r.choice(c_cards)]
        c_cards = card_deck(comp,c_cards)

        player_score = calculate_score(player)
        comp_score = calculate_score(comp)
        print(p_cards)
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Computer's first card: {comp[0]}")

        #Player's turn 
        while player_score < 21:
            choice = input("Type 'y' to get another card, type 'n' to pass : ")
            if choice == 'y':
                player.append(r.choice(p_cards))
                p_cards = card_deck(player,p_cards)
                print(p_cards)
                player_score = calculate_score(player)
                print(f"Your cards: {player}, current score: {player_score}")
                if player_score>21:
                    print("You busted. You lose")
                    break
            else :
                break
         # Computer's turn 
        while comp_score < 22 and comp_score < player_score:
            comp.append(r.choice(c_cards))
            c_cards = card_deck(comp,c_cards)
            comp_score = calculate_score(comp)
        
        print(f"Your final hand : {player}, final score : {player_score}")
        print(f"Computer's final hand : {comp}, final score : {comp_score}")
        
        # Determine winner
        if player_score > 21:
            print("You lost!")
        elif comp_score > 21 or player_score > comp_score:
            print("You win!")
        elif player_score == comp_score:
            print("It's a tie!")
        else:
            print("You lost!")

        check = input("do you wanna play blackjack ? y or n : ")
    

play_blackjack()