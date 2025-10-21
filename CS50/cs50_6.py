# File I/O in Python

# Writes to a file

name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()

# Appends to a file

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# Adds context manager

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# Reads from a file

with open("names.txt") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

# rstrip()  # removes trailing whitespace characters like \n
# or use strip() to remove leading and trailing whitespace
# or use lstrip() to remove leading whitespace only
# rm names.txt  # command to remove the file from terminal
