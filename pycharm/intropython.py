# String Length

phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""  # """ are used to define multi-line strings

index_to_slice = (int(len(phrase)/2))
print(index_to_slice)

first_half = phrase[0:44]  # Get the slice of the phrase.
print(first_half)

###

# backslash usage

dont_worry = "Don't worry about single quotes if the string is in double quotes, and vice versa"
print(dont_worry)

print("\"Sweet\" is an ice-cream")

print('The name of this ice cream is "Sweet\'n\'Tasty"')

###

# String Methods

monty_python = "Monty Python"
print(monty_python)

print(monty_python.lower())    # Print lower-cased version of the string

print(monty_python.upper())

###

# String Formatting

name = "John"
# Note: %s is inside the string, % is after the string.
print("Hello, PyCharm! My name is %s!" % name)

print("I'm %d years old" % 35)

###

name = "Andrea"
age = 35
print(f"Hello, My name is {name} and I'm {age} years old.")

###

squares = [1, 4, 9, 16, 25]   # Create a new list
print(squares)

print(squares[1:4])  # list slicing

###
