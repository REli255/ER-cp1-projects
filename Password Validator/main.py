# Eli Robison, Password Validator

check = 0

def contains_number(value):
    for character in value:
        if character.isdigit():
            return True
    return False

import re
def contains_special(string):
    rex = re.compile("@!#$%^&*<>?~")
    search = rex.search(string)
    if search == None:
        return False
    else:
        return True

while check < 3:
    password = input("enter a password: ")

    if len(password) <= 8:
        check += 1

    if contains_number(password):
        check += 1

    if contains_special(password):
        check += 1

    if check < 3:
        print(password, "does not meet the requirements")   

print(password, "meets the requirements")