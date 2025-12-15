# Regular Expressions or Regex are a sequence of characters that form a search pattern.
# They are used for pattern matching within strings,
# allowing for complex search, replace, and validation operations.
# In Python, the 're' module provides support for regular expressions.
# Used for validating formats like email addresses, phone numbers, and more.
# Common functions include re.match(), re.search(), re.findall(), and re.sub().
# Example: To check if a string is a valid email address.
# Used to define patterns for searching and manipulating strings efficiently.
# Used in data validation, parsing, and text processing tasks.
# Used in web scraping, data cleaning, and input validation.

# Validates email address by checking for . too

import re
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

# Validates email address by checking username and domain separately

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")

# Changes * to +


email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    # if re.search("..*@..*", email): # This would also work, but the + is more precise
    print("Valid")
else:
    print("Invalid")

# Adds \.edu


email = input("What's your email? ").strip()

# Note the r before the string to indicate a raw string, so that \. is treated as a literal dot
if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

# Adds ^ and $ to regex


email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# Adds [^] to regex

email = input("What's your email? ").strip()
# ensures no @ in username or domain, only one @, and [^] means "not"
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# Adds character class


email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# Replaces character class with \w


email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):  # \w is shorthand for [a-zA-Z0-9_]
    print("Valid")
else:
    print("Invalid")

# Adds re.IGNORECASE


email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# Adds optional subdomain


email = input("What's your email? ").strip()

# (\w+\.)? makes the subdomain optional, the ? means "0 or 1"
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# Reformats "last, first" as "first last"

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")

# Uses re.search


name = input("What's your name? ").strip()
# captures last and first names, groups, ^ and $ for start and end, .+ for one or more characters,
# (.+) for capturing a group separated by , and space
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = first + " " + last
print(f"hello, {name}")

# Uses .group


name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    # group(2) is first, group(1) is last
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# Uses walrus operator


name = input("What's your name? ").strip()
# walrus operator :=, assigns and evaluates, so no need for separate if statement
if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# := Walrus operator allows assignment within an expression
# Introduced in Python 3.8
# Used to simplify code by combining assignment and evaluation
# Commonly used in loops and conditional statements
# Example: While reading lines from a file, assign and check in one step
# Used to reduce redundancy and improve readability in certain scenarios
# Used in loops and conditionals to streamline code and enhance clarity
# Used to assign values to variables as part of larger expressions
# Example: While reading lines from a file, assign and check in one step
# while (line := file.readline()) != "":
# print(line)

# Extracts Twitter username from URL using str.replace

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

# Extracts Twitter username from URL using str.removeprefix

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")

# Uses re.sub


url = input("URL: ").strip()

username = re.sub(r"^https://twitter\.com/", "", url)
print(f"Username: {username}")

# Allows for http, no protocol, and www.


url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

# Uses capture group


url = input("URL: ").strip()

# (?:...) is a non-capturing group for www.
matches = re.search(
    r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))

# Ignores query and fragment


url = input("URL: ").strip()

matches = re.search(
    r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))

# Patterns:
# Hexadecimal color code

# import re


def main():
    code = input("Hexadecimal color code: ")

    pattern = r"#"
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid")


main()


def main():
    code = input("Hexadecimal color code: ")

    # starts with # followed by exactly 6 hex digits
    pattern = r"^#[a-fA-F0-9]{6}$"
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid")


main()

# Capturing groups

# import re


locations = {"+1": "United States and Canada",
             "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    pattern = r"\+\d{1,3} \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        print("Valid")
    else:
        print("Invalid")


main()

locations = {"+1": "United States and Canada",
             "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    pattern = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group(1)
        print(locations[country_code])
    else:
        print("Unknown")


main()

locations = {"+1": "United States and Canada",
             "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group("country_code")
        print(locations[country_code])
    else:
        print("Unknown")


main()

# Problem 7 Homework
# NUMB3RS

# implement a function called validate that expects an IPv4 address as input as a str
# and then returns True or False, respectively, if that input is a valid IPv4 address or not.

# An IPv4 address is a numeric identifier that a device (or, on TV, hacker)
# uses to communicate on the internet, akin to a postal address in the real world,
# typically formatted in dot-decimal notation as #.#.#.#
# But each # should be a number between 0 and 255, inclusive.

# import re

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):

    # Pattern to match an IPv4 address format
    pattern = r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})"
    matches = re.search(pattern, ip)
    group_status = []

    if matches:
        for group in matches.groups():
            if int(group) > 255:
                group_status.append(False)
            else:
                group_status.append(True)
    else:
        return False

    if False in group_status:
        return False
    else:
        return True


if __name__ == "__main__":
    main()


# from playground import validate


def main():
    test_format()
    test_range()


def test_format():
    assert validate("233.45.32") is False
    assert validate("cats") is False
    assert validate("...") is False
    assert validate("155.199.100.2") is True
    assert validate("233.45.32.244") is True


def test_range():
    assert validate("300.45.32.244") is False
    assert validate("233.400.32.244") is False
    assert validate("233.45.500.244") is False
    assert validate("233.45.32.600") is False
    assert validate("256.256.256.256") is False


Errors: https: // submit.cs50.io/check50/d55a8d11be603dc937a49fa92c12d9feb33a1e4b


#