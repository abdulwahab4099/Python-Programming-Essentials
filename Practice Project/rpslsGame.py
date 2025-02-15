import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("Error: Invalid choice")
        return None

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Error: Invalid number")
        return None

def rpsls(player_choice):
    print("\nPlayer chooses", player_choice)
    
    player_number = name_to_number(player_choice)
    if player_number is None:
        return
    
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses", comp_choice)
    
    difference = (comp_number - player_number) % 5
    
    if difference == 0:
        print("It's a tie!")
    elif difference in [1, 2]:
        print("Computer wins!")
    else:
        print("Player wins!")

# Test cases
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
