# Eli Robison, simple calculater

symbol = int(input("enter the type equation(1=+, 2=-, 3=*, 4=/ or 5=**): "))

first = int(input("enter the first number: "))
second = int(input("enter the second number: "))

if symbol == 1:
    equation = first+second
else: 
    if symbol == 2:
        equation = first-second
    else: 
        if symbol == 3:
            equation = first*second
        else:
            if symbol == 4:
                equation = round(first/second)
            else:
                equation = first**second

print(equation)