# Conditionals
# Demonstrates chained comparisons

score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# Demonstrates fewer comparisons

score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Demonstrates a function that returns a bool


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()

# Demonstrates conditional expressions (ternary operators)


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False


main()

# Demonstrates returning the value of a Boolean expression


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0

# is_even(2)


main()

# Uses |

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


# Problem 1 Homework
# Deep
question = input(
    "What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

if question == "42":
    print("Yes")
elif question == "forty two" or question == "forty-two":
    print("Yes")
else:
    print("No")

# Bank
greeting = (input("Write your greeting: ").strip().lower())

hello = greeting.startswith("hello")
h = greeting.startswith("h")

if hello == True:
    print("$0")
elif h == True:
    print("$20")
else:
    print("$100")

# File Extensions
file_name = input("File name please: ").strip().lower()

if ".gif" in file_name:
    print("image/gif")
elif ".jpg" in file_name or ".jpeg" in file_name:
    print("image/jpeg")
elif ".png" in file_name:
    print("image/png")
elif ".pdf" in file_name:
    print("application/pdf")
elif ".txt" in file_name:
    print("text/plain")
elif ".zip" in file_name:
    print("application/zip")
else:
    print("application/octet-stream")

# Math Interpreter
expression = input("Expression: ")

x, y, z = expression.split(" ")
x, z = int(x), int(z)

match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        print(float(x / z))
    case _:
        print("try again")

# Meal Time


def main():
    time = input("What time is it? ")
    floattime = convert(time)

    if floattime >= 7 and floattime <= 8:
        print("breakfast time")
    elif floattime >= 12 and floattime <= 13:
        print("lunch time")
    elif floattime >= 18 and floattime <= 19:
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    hours, minutes = int(hours), int(minutes)

    floattime = hours + minutes / 60
    floattime = round(float(floattime), 2)

    return floattime


if __name__ == "__main__":
    main()
