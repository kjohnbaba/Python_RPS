import random

player_wins = 0
bot_wins = 0

rps = ["ROCK", "PAPER", "SCISSORS"]

while True:
    user_input = input("Type either rock paper or scissors to play, or enter Q to quit:  ").upper()
    if user_input == "Q":
        break
    elif user_input not in ["ROCK", "PAPER", "SCISSORS"]:
        print("Typo, please try again")
        continue
    rps_randomizer = random.randint(1, 3)
    # rock = 1, paper = 2, scissors = 3
    pc_selection = rps[rps_randomizer-1]
    print("Bot picked :", pc_selection + " ")

    if user_input == "ROCK" and pc_selection == "SCISSORS":
        print("You win this round")
        player_wins += 1
    elif user_input == "SCISSORS" and pc_selection == "PAPER":
        print("You win this round")
        player_wins += 1
    elif user_input == "PAPER" and pc_selection == "ROCK":
        print("You win this round")
        player_wins += 1
    elif user_input == pc_selection:
        print("Draw")
    else:
        print("You lost this round")
        bot_wins += 1

print("Player wins:", player_wins)
print("Bot wins:", bot_wins)
if player_wins > bot_wins:
    print("YOU WIN")
elif bot_wins > player_wins:
    print("YOU LOST")
else:
    print("DRAW")
print("Game End")
