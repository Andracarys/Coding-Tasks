name = input("name:")
# concatenation: + will not add a space, you need to add it.
print("hi, " + name)
# comma will add a space and it's for multiple variables.
print("hi,", name, name, name)
print("hi,", end="###")  # end changes how the phrase ends
# sep changes the separator value where the comma is used.
print("hi,", name, sep="--- ")
