# Eli Robison, Authorized

authorized = ["fred", "jack", "boss", "manager", "david"]
admin = ["boss", "manager"]
user = ["fred", "jack", "boss", "manager", "david", "hacker", "theif", "villain"]

check = int(input("enter the number of the user you would like to check: ")) - 1

if user[check] in admin:
    print(user[check], "is an admin")
elif user[check] in authorized:
    print(user[check], "is an authorized user")
else:
    print(user[check], "is an unauthorized user")