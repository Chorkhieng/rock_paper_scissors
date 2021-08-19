import random



while True:
    
    choices = ["rock", "paper", "scissors"]

    
    player = None
    player_wins = 0
    computer_wins = 0
    ties = 0
    

    while True:
        player = input("rock, paper, or scissors? Or type stop to exit and get result of the game: ").lower()
        computer = random.choice(choices)
        
        if player == computer:
            print("Computer: ", computer)
            print("Player: ", player)
            print("Tie!")
            player = player
            computer = computer
            ties += 1
        elif player == "rock":
            if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You lost!")
                computer_wins += 1
            if computer == "scissors":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You won!")
                player_wins += 1
        elif player == "paper":
            if computer == "scissors":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You lost!")
                computer_wins += 1
            if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You won!")
                player_wins += 1
        elif player == "scissors":
            if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You lost!")
                computer_wins += 1
            if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You won!")
                player_wins += 1
        elif player.lower() == "stop":
            break

    print("Total play times: ", computer_wins + player_wins + ties)
    print("Computer Won: ", computer_wins, " times!")
    print("You won: ", player_wins, " times!")
    print("You and Computer picked the same choice ", ties, "times.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n\n\n++++++ Final Result +++++++")
if computer_wins == player_wins:
    print("No winner!\nYou and Computer have the same score!")
elif computer_wins < player_wins:
    print("You won!\nYour score is", player_wins - computer_wins, "high than Computer!")
elif computer_wins > player_wins:
    print("Computer won! Computer's score is", computer_wins - player_wins, "higher than yours!")
print("Goodbye!")
    

