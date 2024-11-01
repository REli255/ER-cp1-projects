# Eli Robison, Secret Cypher

message = input("enter the message you would like encrypted: ")

def incrypt(word):
    letters = list(word)
    for x in range(len(word)):
        if word[x] == "a":
            letters[x] = "d"
        elif word[x] == "b":
            letters[x] = "e"
        elif word[x] == "c":
            letters[x] = "f"
        elif word[x] == "d":
            letters[x] = "g"
        elif word[x] == "e":
            letters[x] = "h"
        elif word[x] == "f":
            letters[x] = "i"
        elif word[x] == "g":
            letters[x] = "j"
        elif word[x] == "h":
            letters[x] = "k"
        elif word[x] == "i":
            letters[x] = "l"
        elif word[x] == "j":
            letters[x] = "m"
        elif word[x] == "k":
            letters[x] = "n"
        elif word[x] == "l":
            letters[x] = "o"
        elif word[x] == "m":
            letters[x] = "p"
        elif word[x] == "n":
            letters[x] = "q"
        elif word[x] == "o":
            letters[x] = "r"
        elif word[x] == "p":
            letters[x] = "s"
        elif word[x] == "q":
            letters[x] = "t"
        elif word[x] == "r":
            letters[x] = "u"
        elif word[x] == "s":
            letters[x] = "v"
        elif word[x] == "t":
            letters[x] = "w"
        elif word[x] == "u":
            letters[x] = "x"
        elif word[x] == "v":
            letters[x] = "y"
        elif word[x] == "w":
            letters[x] = "z"
        elif word[x] == "x":
            letters[x] = "a"
        elif word[x] == "y":
            letters[x] = "b"
        elif word[x] == "z":
            letters[x] = "c"
        else:
            pass
    return str(letters)

print(incrypt(message))