# Eli Robison, Password Validator

check = 0

while check == 0:
    password = input("enter a pasaword: ")

    if len(password) <= 8:
        check = check + 1
    elif any(password):
        check = check + 1