# Eli Robison, What are these numbers?

number = int(input("enter a number: "))
comma = "Your number with commas to separate the thousands is '{:,}'."
decimal = "Your number with 4 decimal places is '{:.4f}'."
percentage = "Your number as a percent is '{:%}'."
dollar = "Your number as  a dollar amount is '${:,.2f}'."

print(comma.format(number))
print(decimal.format(number))
print(percentage.format(number))
print(dollar.format(number))