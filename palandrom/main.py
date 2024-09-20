# Eli Robison, Palandrom

w = input("enter a word: ")
r = w[::-1]

if w == r:
    print(w, "is a palandrom")
else:
    print(w, "is not a palandrom")