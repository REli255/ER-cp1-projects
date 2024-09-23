#Eli Robison, graded quiz

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