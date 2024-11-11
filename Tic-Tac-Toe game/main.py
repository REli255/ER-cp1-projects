# Eli Robison, Tic-Tac-Toe game

def check(letter):
    for x in range(3):
        for y in range(3):
            x, y, letter

cross = "X"
circle = "O"

if check(cross):
    print("you won")
elif check(circle):
    print("you lost")