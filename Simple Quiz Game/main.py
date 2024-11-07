# Eli Robison, ProficiencyTest: Simple Quiz Game

easy_questions = ["Is Zombicide a CMON game?", "Is Is Monopoly a CMON game?", "Is Cthulhu: Death May Die a CMON game?"]
normal_questions = ["Is Blood Rage a CMON game?", "Is Code Names a CMON game?", "Is Seven Wonders a CMON game?"]
hard_questions = ["How many miniatures are in the Zombicide: Undead or Alive core box?", "How many miniatures are in the Cthulhu: Death May Die - Fear of the Unknown core box?", "How many miniatures are in the Massive Darkness 2: Hellscape core box?"]
questions = [easy_questions, normal_questions, hard_questions]

easy_answers = ["yes", "no", "yes"]
normal_answers = ["yes", "no", "no"]
hard_answers = ["88", "46", "68"]
answers = [easy_answers, normal_answers, hard_answers]

score = 0

for x in range(len(questions)):
    for y in range(len(questions[x])):
        guess = input(questions[x][y])
        if guess == answers[x][y]:
            score += 1
            print("you were right")
        else:
            print("you were wrong")
        total = len(questions) * len(questions[x])

print("score is", score, "out of", total)