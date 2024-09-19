# Eli Robison, Palandrom

w = input("enter a seven letter word: ")
r = str(w[-1] + w[-2] + w[-3] + w[-4] + w[-5] + w[-6] + w[-7])

if w == r:
    print(w, "is a palandrom")
else:
    print(w, "is not a palandrom")