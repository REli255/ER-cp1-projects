# Eli Robison, FINAL PROJECT

import random

while True:
    while True:
        races = ["human", "elf", "goblin", "orc"]
        classes = ["berserker", "fighter", "ranger", "wizard"]
        
        name = input("enter the name of your character: ")
        
        race = int(input("enter the race of your character (1=human, 2=elf, 3=goblin, 4=orc): "))
        if race == 1:
            race = races[0]
            health = 11
            strength = 11
            dexterity = 11
            intelligence = 11
        elif race == 2:
            race = races[1]
            health = 12
            strength = 10
            dexterity = 12
            intelligence = 11
        elif race == 3:
            race = races[2]
            health = 9
            strength = 11
            dexterity = 14
            intelligence = 10
        else:
            race = races[3]
            health = 13
            strength = 14
            dexterity = 8
            intelligence = 9
        
        job = int(input("enter the class of your character (1=berserker, 2=fighter, 3=ranger, 4=wizard): "))
        if job == 1:
            job = classes[0]
            health += 2
            strength += 4
            dexterity -= 1
            intelligence -= 1
        elif job == 2:
            job = classes[1]
            health += 1
            strength += 1
            dexterity += 1
            intelligence += 1
        elif job == 3:
            job = classes[2]
            health += 0
            strength -= 1
            dexterity += 4
            intelligence += 1
        else:
            job = classes[3]
            health += 1
            strength -= 1
            dexterity -= 1
            intelligence += 5
        
        print(name, "is a", race, job, "with", health, "health,", strength, "strength,", dexterity, "dexterity and", intelligence, "intelligence")
        
        def puzzle():
            puzzles = ["math", "Tic Tac Toe", "spotting", "Rock Paper Scissors"]
            problem = random.choice(puzzles)
            if problem == "math":
                score = 0
                question_a = int(input("what does 9*8 equal: "))
                question_b = int(input("what does 65+78 equal: "))
                question_c = int(input("what does 54*3 equal: "))
                question_d = int(input("what does 33-56 equal: "))
                question_e = int(input("what does 132/11 equal: "))
                answer_a = 72
                answer_b = 153
                answer_c = 162
                answer_d = -23
                answer_e = 12
                if question_a == answer_a:
                    score += 1
                if question_b == answer_b:
                    score += 1
                if question_c == answer_c:
                    score += 1
                if question_d == answer_d:
                    score += 1
                if question_e == answer_e:
                    score += 1
                print("your score is", score, "out of 5")
                if score <= 3:
                    print("you beat the puzzle")
                else:
                    health -= 1
            if problem == "Tic Tac Toe":
                board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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
                while turns < 9 and winner != "you won" and winner != "you lost":
                    for x in range(rows):
                        for y in range(columns):
                            print("", board[x][y], end= " |")
                        print("")
                    if turns in even:
                        print("player's turn")
                        player = int(input("enter the number of where you would like to play: "))
                        if player in numbers:
                            if player == 1:
                                board[0][0] = "X"
                                numbers.remove(player)
                                turns += 1
                            elif player == 2:
                                board[0][1] = "X"
                                numbers.remove(player)
                                turns += 1
                            elif player == 3:
                                board[0][2] = "X"
                                numbers.remove(player)
                                turns += 1
                            elif player == 4:
                                board[1][0] = "X"
                                numbers.remove(player)
                                turns += 1
                            elif player == 5:
                                board[1][1] = "X"
                                numbers.remove(player)
                                turns += 1
                            elif player == 6:
                                board[1][2] = "X"
                                numbers.remove(player)
                                turns += 1
                            elif player == 7:
                                board[2][0] = "X"
                                numbers.remove(player)
                                turns += 1
                            elif player == 8:
                                board[2][1] = "X"
                                numbers.remove(player)
                                turns += 1
                            elif player == 9:
                                board[2][2] = "X"
                                numbers.remove(player)
                                turns += 1
                            else:
                                print("that is not an option")
                        else:
                            print("that is not an option")
                    else:
                        print("computer's turn")
                        computer = random.choice(numbers)
                        if computer == 1:
                            board[0][0] = "O"
                        elif computer == 2:
                            board[0][1] = "O"
                        elif computer == 3:
                            board[0][2] = "O"
                        elif computer == 4:
                            board[1][0] = "O"
                        elif computer == 5:
                            board[1][1] = "O"
                        elif computer == 6:
                            board[1][2] = "O"
                        elif computer == 7:
                            board[2][0] = "O"
                        elif computer == 8:
                            board[2][1] = "O"
                        elif computer == 9:
                            board[2][2] = "O"
                        turns += 1
                        numbers.remove(computer) 
                winner = check()
                for x in range(rows):
                    for y in range(columns):
                        print("", board[x][y], end= " |")
                    print("")
                print(winner)
                if winner == "you won":
                    print("you beat the puzzle")
                else:
                    health -= 1
            if problem is spotting:
                have the player find how many letter d there is
            if problem is Rock Paper Scissors:
                have the player play a game of rock paper scissors
        Display “you are at your home and need to complete a puzzle to move on.”
        Have the player do a puzzle()
        Initialize “choice” variable to Get where the player wants to go
        Function fight()
        Initialize “enemies” variable to [Goblin, Minotaur, Obsidian Golem, Lava Titan, Water Titan]
        If choice is storm village
        Initialize “enemy” variable to enemies[0]
        Else If choice is canyon village
        Initialize “enemy” variable to enemies[1]
        Else If choice is obsidian village
        Initialize “enemy” variable to enemies[2]
        Else If choice is volcano cloud
        Initialize “enemy” variable to enemies[3]
        Else If choice is ocean cloud
        Initialize “enemy” variable to enemies[4]
        Display “you will now fight” enemy
        Have the player fight enemy
        if health is 0 or less
        Display “you died”
        Break
        If choice is storm village
        Display “you are at storm village and need to complete a fight to get an item and move on.”
        Have the player do a fight()
        If choice is rain village
        Display “you are at rain village and need to complete a puzzle to get an item and move on.”
        Have the player do a puzzle()
        Initialize “choice” variable to Get where the player wants to go
        If choice is desert village
        Display “you are at desert village and need to complete a puzzle to move on.”
        Have the player do a puzzle()
        If choice is canyon village
        Display “you are at canyon village and need to complete a fight to move on.”
        Have the player do a fight()
        If choice is mountain village
        Display “you are at mountain village and need to complete a puzzle to get an item and move on.”
        Have the player do a puzzle()
        Initialize “choice” variable to Get where the player wants to go
        If choice is obsidian village
        isplay “you are at obsidian village and need to complete a fight to get an item and move on.”
        Have the player do a fight()
        If choice is beach village
        Display “you are at beach village and need to complete a puzzle to get an item and move on.”
        Have the player do a puzzle()
        Initialize “choice” variable to Get where the player wants to go
        If choice is volcano cloud
        Display “you are at storm village and need to defeat the lava titan to win the game.”
        Have the player do a fight()
        If player won the fight
        Display “you beat the game”
        If choice is ocean cloud
        Display “you are at storm village and need to defeat the water titan to win the game.”
        Have the player do a fight()
        If player won the fight
        Display “you beat the game”
        Break 
        Initialize “again” variable to Get if the player wants to play again
        If again is yes
        Display “starting over”
        Else 
        Break 
