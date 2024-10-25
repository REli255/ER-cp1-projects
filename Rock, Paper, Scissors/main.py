# Eli Robison, Rock, Paper, Scissors

import random


choose = input("would you like to play Rock, Paper, Scissors?: ")
rps = ["Rock", "Paper", "Scissors"]
bot_wins = 0
player_wins = 0

while choose == "yes":
    man = int(input("enter 1 for Rock, 2 for Paper or 3 for Scissors: "))
    if man == 1:
        pass
    elif man == 2:
        pass
    elif man == 3:
        pass
    else:
        print("that is not an option please try again")
        continue
    bot = random.choice(rps)
    if man == 1 and bot == "Rock":
        winner = "you tied"
    elif man == 1 and bot == "Paper":
        winner = "you lost"
    elif man == 1 and bot == "Scissors":
        winner = "you won"
    elif man == 2 and bot == "Rock":
        winner = "you won"
    elif man == 2 and bot == "Paper":
        winner = "you tied"
    elif man == 2 and bot == "Scissors":
        winner = "you lost"
    elif man == 3 and bot == "Rock":
        winner = "you lost"
    elif man == 3 and bot == "Paper":
        winner = "you won"
    else:
        winner = "you tied"
    if winner == "you won":
        player_wins = player_wins + 1
    elif winner == "you lost":
        bot_wins = bot_wins + 1
    else:
        pass
    
    print("you picked", rps[man - 1], "and the bot picked", bot)
    print(winner)
    print("you have won", player_wins, "times and lost", bot_wins, "times")
    
    again = input("would you like to play another round of Rock, Paper, Scissors?: ")
    
    if again == "no":
        break