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
            health = 31
            strength = 11
            dexterity = 11
            intelligence = 11
        elif race == 2:
            race = races[1]
            health = 32
            strength = 10
            dexterity = 12
            intelligence = 11
        elif race == 3:
            race = races[2]
            health = 29
            strength = 11
            dexterity = 14
            intelligence = 10
        else:
            race = races[3]
            health = 33
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
        stats = ("you have", health, "health,", strength, "strength,", dexterity, "dexterity and", intelligence, "intelligence")
        
        def puzzle():
            print(stats)
            health = stats[3]
            puzzles = ["math", "Tic Tac Toe", "Rock Paper Scissors"]
            problem = random.choice(puzzles)
            if problem == "math":
                score = 0
                question_a = int(input("what does 9*8 equal: "))
                question_b = int(input("what does 65+78 equal: "))
                question_c = int(input("what does 54*3 equal: "))
                question_d = int(input("what does 33-56 equal: "))
                question_e = int(input("what does 132/11 equal: "))
                answer_a = 72
                answer_b = 143
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
                if score >= 3:
                    print("you beat the puzzle")
                else:
                    health -= 3
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
                    health -= 2
            if problem == "Rock Paper Scissors":
                rps = ["Rock", "Paper", "Scissors"]
                man = int(input("enter 1 for Rock, 2 for Paper or 3 for Scissors: "))
                while True:
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
                    print("you picked", rps[man - 1], "and the bot picked", bot)
                    print(winner)
                    if winner == "you won":
                        print("you beat the puzzle")
                    else:
                        health -= 2
                    break
        
        def items():
            things = ["knife", "club", "potion"]
            item = random.choice(things)
            health = stats[3]
            strength = stats[5]
            if item == things[0]:
                print("you got a", things[0], "which increases your strength by 3")
                strength += 3
            elif item == things[1]:
                print("you got a", things[1], "which increases your strength by 5")
                strength += 5
            else:
                print("you got a", things[2], "which increases your health by 5")
                health += 5
            print(stats)
        
        print("you are at your home and need to complete a puzzle to move on.")
        puzzle()
        if health <= 0:
                print("you died")
                break

        choice = int(input("enter where you want to go next(1 = storm village, 2 = rain village): "))

        def fight():
            enemies = ["Goblin", "Minotaur", "Obsidian Golem", "Lava Titan", "Water Titan"]
            health = stats[3]
            if choice == 1:
                enemy = enemies[0]
                e_stats = 8
                e_health = 10
            elif choice == 4:
                e_stats = 9
                e_health = 12
                enemy = enemies[1]
            elif choice == 6:
                enemy = enemies[2]
                e_stats = 10
                e_health = 10
            elif choice == 8:
                enemy = enemies[3]
                e_stats = 13
                e_health = 22
            elif choice == 9:
                enemy = enemies[4]
                e_stats = 12
                e_health = 24
            
            e_state = ("the", enemy, "has", e_health, "health and", e_stats, "strength")
            print("you will now fight", enemy)
            while health > 0 and e_health > 0:
                print(stats)
                print(e_state)
                dodge = input("do you want to attack or dodge: ")
                health = stats[3]
                if dodge == "attack":
                    health -= e_stats
                    e_health -= strength
                else:
                    health += 3
                    e_health += 2
            if health <= 0:
                pass
            else:
                print ("you won the fight")
        
        if choice == 1:
            print("you are at storm village and need to complete a fight to get an item and move on.")
            fight()
            items()
        if choice == 2:
            print("you are at rain village and need to complete a puzzle to get an item and move on.")
            puzzle()
            items()
        if health <= 0:
                print("you died")
                break

        choice = int(input("enter where you want to go next(3 = desert village, 4 = canyon village, 5 = mountain village): "))
        if choice == 3:
            print("you are at desert village and need to complete a puzzle to move on.")
            puzzle()
        if choice == 4:
            print("you are at canyon village and need to complete a fight to get move on.")
            fight()
        if choice == 5:
            print("you are at mountain village and need to complete a puzzle to move on.")
            puzzle()
        if health <= 0:
                print("you died")
                break

        choice = int(input("enter where you want to go next(6 = obsidian village, 7 = beach village): "))
        if choice == 6:
            print("you are at obsidian village and need to complete a fight to get an item and move on.")
            fight()
            items()
        if choice == 7:
            print("you are at beach village and need to complete a puzzle to get an item and move on.")
            puzzle()
            items()
        if health <= 0:
                print("you died")
                break

        choice = int(input("enter where you want to go next(8 = volcano cloud, 9 = ocean cloud): "))
        if choice == 8:
            print("you are at the volcano cloud and need to defeat the lava titan to win the game.")
            fight()
        if choice == 9:
            print("you are at the ocean cloud and need to defeat the water titan to win the game.")
            fight()
        if health > 0:
            print("you beat the game")
        else:
            print("you died")
            break
        
        break 

    again = input("do you want to play again (yes or no): ")
    if again == "yes":
        print("starting over")
    else:
        print("thank you for playing")
        break