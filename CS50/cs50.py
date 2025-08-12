# Working with str
name = input("name:").strip().title()
# concatenation: + will not add a space, you need to add it.
print("hi, " + name)
# comma will add a space and it's for multiple variables.
print("hi,", name, name, name)
print("she is", "A")
print("she is " + "A")  # concatenation
print(f"she is {name}")  # format string / f-string

# str methods
# name = name.strip()  # removes whitespace from str
# name = name.capitalize()  # capitalizes the first letter of the str
# name = name.title() # capitalizes the first letter of every word of the str
# name = name.strip().title() # chaining functions together

print("hi,", end="###\n")  # end changes how the phrase ends
# sep changes the separator value where the comma is used.
print("hi", name, sep=" --- ")
print("hello there 'friend'")  # how to add quotes to a string
print("hello there \"friend\"")  # Backslash is called an escape character

# splits the str using what's inside the quotes as a separator
first, last = name.split(" ")
print(f"she is {first}")

###

# Working with int
x = int(input("name x: "))
y = int(input("name y: "))
print(x + y)
