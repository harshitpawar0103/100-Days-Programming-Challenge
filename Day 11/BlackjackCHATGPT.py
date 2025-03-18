import random as r

def calculate_score(hand):
    """Calculate the total score of a hand, handling Aces dynamically."""
    score = sum(card if card != "Ace" else 11 for card in hand)
    # Adjust Ace value if needed
    for i in range(len(hand)):
        if score > 21 and hand[i] == "Ace":
            score -= 10  # Convert 11 to 1
    return score

def play_blackjack():
    """Main game loop for Blackjack."""
    check = input("Do you want to play Blackjack? (y/n): ").lower()
    
    while check == 'y':
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "Ace"]
        player = [r.choice(cards), r.choice(cards)]
        computer = [r.choice(cards), r.choice(cards)]
        
        player_score = calculate_score(player)
        computer_score = calculate_score(computer)
        
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Computer's first card: {computer[0]}")

        # Player's Turn
        while player_score < 21:
            choice = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if choice == 'y':
                player.append(r.choice(cards))
                player_score = calculate_score(player)
                print(f"Your cards: {player}, current score: {player_score}")
                if player_score > 21:
                    print("You busted! You lose.")
                    break
            else:
                break
        
        # Computer's Turn
        if player_score <= 21:
            while computer_score < 17:
                computer.append(r.choice(cards))
                computer_score = calculate_score(computer)
        
        print(f"Your final hand: {player}, final score: {player_score}")
        print(f"Computer's final hand: {computer}, final score: {computer_score}")

        # Determine winner
        if player_score > 21:
            print("You lost!")
        elif computer_score > 21 or player_score > computer_score:
            print("You win!")
        elif player_score == computer_score:
            print("It's a tie!")
        else:
            print("You lost!")

        check = input("Do you want to play again? (y/n): ").lower()

play_blackjack()
