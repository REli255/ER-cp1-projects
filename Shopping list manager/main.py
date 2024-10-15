# Eli Robison, Shopping list manager

shop = []

def add():
    shop.append(input("enter an item you would like to add to the list: "))

def remove():
    index = int(input("enter the number of the item yuo would like to remove: ")) - 1
    shop.remove(shop[index])

while True:

    action = input("""What would you like to do?

                                  Enter 1 to add item

                                  Enter 2 to remove item

                                  Enter 3 to leave the list:\n""")

    if action =="1":

        add()
        print("your current list is", shop)

    elif action =="2":

        remove()
        print("your current list is", shop)

    else:

        print("your final list is",shop)
        print("Have a nice day!")

        break