# Eli Robison, average grade

p = int(input("enter probraming grade: "))
g = int(input("enter geography grade: "))
a = int(input("enter advisory grade: "))
m = int(input("enter math grade: "))
b = int(input("enter biology grade: "))
e = int(input("enter english grade: "))

average = round((p+g+a+m+b+e)/6)

name = input("enter name: ")

print(name,"'s average grade is",average,"%")