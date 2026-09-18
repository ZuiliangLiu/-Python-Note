import random

options = ["rock","paper","scissors"]

computer = random.choice(options)
playing = True
player = input("Player choose rock, paper, or scissors:")
while playing:
    if player not in options:
        player = (input("Your options is valid value.Please choose rock, paper, or scissors:"))

    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print ("You win")
    elif player == "paper" and computer == "rock":
        print ("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print ("You lose")
    play_again = input("Do you want to play again?(Y/N)")
    if play_again == "N":
         playing = False
print(f"Player choose {player}")
print(f"Computer choose {computer}")










