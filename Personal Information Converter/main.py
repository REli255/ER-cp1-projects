# Eli Robison, Personal Information Converter

name = input("enter your name: ")
age = input("enter your age: ")
height = input("enter your height in meters: ")
favorite = input("enter your favorite number: ")

print("the original is", name, age, height, favorite)

name_c = name
age_c = int(age)
height_c = float(height)
favorite_c = int(favorite)

print("the converted is", name_c, age_c, height_c, favorite_c)