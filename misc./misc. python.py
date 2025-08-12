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
