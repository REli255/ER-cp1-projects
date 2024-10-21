# Eli Robison, What is My Grade

classes = int(input("enter the number of classes you take: "))

for c in range(classes):
    course = input("enter the name of your class: ")
    grade = input("enter you grade persentage: ")

    if grade > 90:
        print("you have an A in", course)
    elif grade > 80:
        print("you have a B in", course)
    elif grade > 70:
        print("you have a C in", course)
    elif grade > 60:
        print("you have a D in", course)
    else:
        print("you have an F in", course)