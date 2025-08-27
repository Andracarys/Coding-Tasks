# Loops
# Demonstrates (more succinct) incrementation

i = 0
while i < 3:
    print("meow")
    i += 1

# Demonstrates a for loop, using a list

for i in [0, 1, 2]:
    print("meow")

# Demonstrates a for loop, using range

for i in range(3):
    print("meow")

# Demonstrates str multiplication

print("meow\n" * 3, end="")

# Introduces continue, break

while True:
    n = int(input("What's n? "))
    if n <= 0:
        continue
    else:
        break

for _ in range(n):
    print("meow")

# Removes continue

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

# Demonstrates defining functions


def main():
    meow(get_number())


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 1:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()

# Demonstrates iterating over a list

students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

# Demonstrates iterating over and indexing into a list

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

# Demonstrates indexing into a dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

# Demonstrates iterating over and index into a dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

# Demonstrates iterating over a list of dict objects

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# Prints square of bricks using a function with nested loops


def main():
    print_square(3)


def print_square(size):
    for i in range(size):  # this one is for the columns
        for j in range(size):  # this one is for the rows
            print("#", end="")  # this leaves the end without a new line
        print()  # this print is here to jump to a new line after the previous one


main()

# Prints square of bricks using a function with a loop and str multiplication


def main():
    print_square(3)


def print_square(size):
    for _ in range(size):
        print("#" * size)


main()

# Prints square of bricks using a function with a loop and str multiplication


def main():
    print_square(3)


def print_square(size):
    for _ in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()

# Problem 2 Homework
# camel

camelCase = input("camelCase: ")
snake_case = ""  # empty string

for char in camelCase:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char

print("snake_case: " + snake_case)

# coke

due = 50

while due > 0:
    print("Amount Due: " + str(due))
    insert = input("Insert coin: ")
    if int(insert) in [25, 10, 5]:
        due -= int(insert)

print("Change Owed: " + str(abs(due)))

# twttr

input = input("input: ")
new_input = ""

for char in input:
    if char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        continue
    else:
        new_input += char

print(new_input)

# Plates


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    pipeline = [rule1, rule2, rule3, rule4]

    for function in pipeline:
        if function(s) == False:
            return False

    return True


def rule1(s):
    chars = 0
    for char in s:
        chars += 1
    # print(chars)

    if chars >= 2 and chars <= 6:  # Rule 1
        return True
    else:
        return False


def rule2(s):
    first_two = s[0:2]

    if first_two.isalpha():  # Rule 2
        return True
    else:
        return False


def rule3(s):
    if s.isalnum():
        return True
    else:
        return False


def rule4(s):
    found_number = False

    for char in s:
        if char.isdigit():
            if not found_number:
                if char == '0':
                    return False  # First number can't be '0'
                found_number = True
        elif found_number:
            return False  # A letter was found after a number

    return True  # If the loop finishes, the rule passes


main()

# nutrition
input = input("Item: ").lower()

fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80"
}

if input in fruits:
    key = input
    print(f"Calories: {fruits[key]} ")
else:
    print("")
