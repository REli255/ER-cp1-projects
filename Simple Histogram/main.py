# Eli Robison, Simple Histogram

for x in range(6):
    number = int(input("enter a number to be made into the histogram:"))
    print(x+1,":", end= " ")
    for y in range(number):
        print("*", end= "")
    print("")