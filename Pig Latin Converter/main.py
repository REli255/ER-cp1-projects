# Eli Robison, Pig Latin Converter

def igpay():
    word = input("enter a word: ")
    pig = (word[1:] + word[0] + "ay")
    return(pig)

print(igpay())