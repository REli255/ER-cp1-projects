# Eli Robison, Tic-Tac-Toe game

board = [[1, 2, 3][4, 5, 6][7, 8, 9]]
def check()
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
Return you won
If board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
Return you won
If board[2][0] is X and board[2][1] is X and board[2][2] is X":
Return you won
If board[0][0] is X and board[1][0] is X and board[2][0] is X":
Return you won
If board[0][1] is X and board[1][1] is X and board[2][1] is X":
Return you won
If board[0][2] is X and board[1][2] is X and board[2][2] is X":
Return you won
If board[0][0] is X and board[1][1] is X and board[2][2] is X":
Return you won
If board[2][0] is X and board[1][1] is X and board[0][2] is X
Return you won
If board[0][0] is O and board[0][1] is O and board[0][2] is O
Return you lost
If board[1][0] is O and board[1][1] is O and board[1][2] is O
Return you lost
If board[2][0] is O and board[2][1] is O and board[2][2] is O
Return you lost
If board[0][0] is O and board[1][0] is O and board[2][0] is O
Return you lost
If board[0][1] is O and board[1][1] is O and board[2][1] is O
Return you lost
If board[0][2] is O and board[1][2] is O and board[2][2] is O
Return you lost
If board[0][0] is O and board[1][1] is O and board[2][2] is O
Return you lost
If board[2][0] is O and board[1][1] is O and board[0][2] is O
Return you lost
End Function

winner = "game"

While winner is not you won or you lost
For y = squares in column
Get where the player wants to play
Generate where the computer plays
Initialize “winner” variable to check()

print(winner)