import random


def get_choice():
    player_choice = input("Enter you choice for the game: ")
    options = ["rock", "scissors", "paper"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a draw"
    elif player == "rock":
        if computer == "scissors":
            return "Rocks Smashes scissors! You win !!!!"
        else:
            return "Paper covers rock. You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win !!!"
        else:
            return "Scissors cuts paper. You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!!!!!"
        else:
            return "Rock smashes scissors. You lose."


choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)
