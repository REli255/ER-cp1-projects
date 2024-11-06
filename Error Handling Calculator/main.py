# Eli Robison, Error Handling Calculator

symbol = input("enter the type equation(1=+, 2=-, 3=*, 4=/ or 5=**): ")

first = input("enter the first number: ")
second = input("enter the second number: ")

try:
    if int(symbol) == 1:
        equation = int(first)+int(second)
    else:
        if int(symbol) == 2:
            equation = int(first)-int(second)
        else: 
            if int(symbol) == 3:
                equation = int(first)*int(second)
            else:
                if int(symbol) == 4:
                    equation = round(int(first)/int(second))
                else:
                    equation = int(first)**int(second)
    print(equation)
except:
    print("you did not enter numbers")