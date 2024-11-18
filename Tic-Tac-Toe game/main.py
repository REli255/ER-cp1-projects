# Eli Robison, Tic-Tac-Toe game

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
columns = 3

def check():
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        return "you won"
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        return "you won"
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        return "you won"
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return "you won"
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return "you won"
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return "you won"
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "you won"
    elif board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
        return "you won"
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        return "you lost"
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        return "you lost"
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        return "you lost"
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return "you lost"
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return "you lost"
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return "you lost"
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "you lost"
    elif board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
        return "you lost"
    else:
        return "you tied"

turns = 0
winner = check()
even = [0, 2, 4, 6, 8]

while turns < 9 and :
    for x in range(rows):
        for y in range(columns):
            print(board[x][y])
    if turns is even:
        player = int(input("enter the number of where you wold like to play: "))
    else:
        computer = O
    turns += 1
    winner = check()
    break

winner = check()
print(winner)