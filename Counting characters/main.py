# Eli Robison

grid = [ ['A', 'B', 'C', 'A', 'D'],
['C', 'A', 'B', 'D', 'E'],
['A', 'D', 'C', 'E', 'A'],
['B', 'A', 'C', 'A', 'D'],
['D', 'C', 'B', 'E', 'A'] ]

letters = ['A', 'B', 'C', 'D', 'E']

for x in range(len(letters)):
    letter = letters[x]
    for y in range(1):
        amount = grid.count(letter, 0, 100)
        print(amount)