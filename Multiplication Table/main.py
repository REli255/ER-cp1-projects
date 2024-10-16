# Eli Robison, Multiplication Table

number = int(input("enter the number you would like multiples of: "))

for x in range(13):
    print(number, "*", x,"=", number * x)