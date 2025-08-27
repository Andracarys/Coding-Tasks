# Encontra el mayor de tres numeros

a = 100
b = 500
c = 200

mayor = max(a, b, c)
print(mayor)

# -----------------------------

lista = [a, b, c]
major = a  # mayor por defecto

for num in lista:
    if num > major:
        major = num

print(major)

###

# strip function

phrase = " hello world "
phrase2 = phrase.strip()
print(phrase2)

text = "**python**"
text2 = text.strip("*")
print(text2)

###

# split function

text3 = "Python is awesome"
words = text3.split()
print(words)

###

# zip function

userids = ["user1", "user2", "user3"]
passwords = [123, 1234, 12345]

# creates tuples with the user id and its password
credentials = zip(userids, passwords)

print(type(credentials))

for i in credentials:  # allows you to see each tuple
    print(i)

# dict function

# stores the user id as a key and its password as a value
credentials = dict(zip(userids, passwords))
print(credentials)

###

# splits the sting into a list of characters
print(list("abc"))

###

x = [1, 2, 3]
y = x.copy()  # copies the list as it is
# y[1] = 99
print(x)
print(y)

###

fruit = "banana"

# counts how many times the paramenter happens in a variable
a = fruit.count("a")
na = fruit.count("na")

print(a)
print(na)

###

# For Loop Example: Multiplication Table

num = int(input("Enter a number: "))

print(f"\nMultiplication Table of {num}:\n")

for _ in range(1, 11):  # loop from 1-10
    print(f"{num} x {_} = {num * _}")
# print("") # creates a blank space
print()  # creates a blank space because \n is already within print's function

# This is not failproof. Needs to be checked!

# Name - maximum character will be 10
# Name must not contain spaces
# Name must not contain digits

name = input("Enter your name: ")

if len(name) > 10:
    print("Name can't be more than 10 characters.")

elif not name.find(" ") == 0:
    print("Name must not contain spaces.")

elif not name.isalpha():
    print("Name must not contain digits.")

elif name.islower():
    print("Name must be in capitalize form.")

else:
    print(f"{name} is your new name.")

###

# String methods in python

name = input("Enter name: ")

length = len(name)  # counts characters including spaces

# finds the index(location) of the parameter's first occurrence
find = name.find("a")

# finds the index(location) from the opposite side, reverse find
reverse_find = name.rfind("a")

capitalize = name.capitalize()  # capitalizes the first letter in the name

isdigit = name.isdigit()  # check if there are only numbers, it is a boolean

# check if there are only alphabetic characters, it is a boolean
isalpha = name.isalpha()

count = name.count("a")  # counts how many times the character appears

print(f"This is the result: {isalpha} ")  # Add a {} with the method to test it

###
