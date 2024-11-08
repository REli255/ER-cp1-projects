# Eli Robison, Character Creator

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