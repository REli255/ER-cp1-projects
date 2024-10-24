# Eli Robison, Rock, Paper, Scissors

import random


choose = input("would you like to play Rock, Paper, Scissors?: ")
rps = ["Rock", "Paper", "Scissors"]

while choose == "yes":
    man = int(input("enter 1 for Rock, 2 for Paper or 3 for Scissors: "))
    bot = random.choice(rps)
    if man == 1 and bot == "Rock":
        winner = "you tied"
    elif man == 1 and bot == "Paper":
        winner = "you tied"
    elif man == 1 and bot == "Scissors":
        winner = "you tied"
    elif man == 2 and bot == "Rock":
        winner = "you won"
    elif man == 2 and bot == "Paper"":
        winner = "you tied"
    elif man == 2 and bot == "Scissors":
        winner = "you tied"
    elif man == 3 and bot == "Rock":
        winner = "you tied"
    elif man == 3 and bot == "Paper"":
        winner = "you tied"
    else:
        winner = "you tied"
    print("you picked", rps[man - 1], "and the bot picked", bot)
    print(winner)
    again = input("would you like to play another round of Rock, Paper, Scissors?: ")
    if again == "no":
        break