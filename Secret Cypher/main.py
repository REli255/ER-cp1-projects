# Eli Robison, Secret Cypher

message = input("enter the message you would like encrypted: ")

def incrypt(word):
    letters = list(word)
    for x in range(len(word)):
        if word[x] == "a" or word[x] == "A":
            letters[x] = "d"
        elif word[x] == "b" or word[x] == "B":
            letters[x] = "e"
        elif word[x] == "c" or word[x] == "C":
            letters[x] = "f"
        elif word[x] == "d" or word[x] == "D":
            letters[x] = "g"
        elif word[x] == "e" or word[x] == "E":
            letters[x] = "h"
        elif word[x] == "f" or word[x] == "F":
            letters[x] = "i"
        elif word[x] == "g" or word[x] == "G":
            letters[x] = "j"
        elif word[x] == "h" or word[x] == "H":
            letters[x] = "k"
        elif word[x] == "i" or word[x] == "I":
            letters[x] = "l"
        elif word[x] == "j" or word[x] == "J":
            letters[x] = "m"
        elif word[x] == "k" or word[x] == "K":
            letters[x] = "n"
        elif word[x] == "l" or word[x] == "L":
            letters[x] = "o"
        elif word[x] == "m" or word[x] == "M":
            letters[x] = "p"
        elif word[x] == "n" or word[x] == "N":
            letters[x] = "q"
        elif word[x] == "o" or word[x] == "O":
            letters[x] = "r"
        elif word[x] == "p" or word[x] == "O":
            letters[x] = "s"
        elif word[x] == "q" or word[x] == "Q":
            letters[x] = "t"
        elif word[x] == "r" or word[x] == "R":
            letters[x] = "u"
        elif word[x] == "s" or word[x] == "S":
            letters[x] = "v"
        elif word[x] == "t" or word[x] == "T":
            letters[x] = "w"
        elif word[x] == "u" or word[x] == "U":
            letters[x] = "x"
        elif word[x] == "v" or word[x] == "V":
            letters[x] = "y"
        elif word[x] == "w" or word[x] == "W":
            letters[x] = "z"
        elif word[x] == "x" or word[x] == "X":
            letters[x] = "a"
        elif word[x] == "y" or word[x] == "Y":
            letters[x] = "b"
        elif word[x] == "z" or word[x] == "Z":
            letters[x] = "c"
        else:
            pass
    secret = ''.join(letters)
    return secret

print(incrypt(message))