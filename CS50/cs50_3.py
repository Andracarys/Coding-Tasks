# Exception handling
# Demonstrates else

try:
import re
x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

###

# Adds a loop

while True:
    try:
        x = int(input("What's x? "))
        # break
    except ValueError:
        print("x is not an integer")
    else:  # if things go right
        break

print(f"x is {x}")

###

# Adds functions, uses break and return


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()

###

# Removes else


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")


main()

###

# Adds pass


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass


main()

###

# Adds prompt


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()

# Problem 3 Homework
# fuel

while True:
    try:
        fraction = input("Fraction: ")
        sectioning = fraction.split("/", 2)
        x, y = sectioning

        step_1 = int(x) / int(y)
        step_2 = round(step_1 * 100)
        step_3 = str(step_2) + "%"

        if int(x) > int(y):
            continue
        elif int(x) < 0 or int(y) < 0:
            continue
        elif step_2 <= 1:
            print("E")
        elif step_2 >= 99:
            print("F")
        else:
            print(step_3)

        break

    except (ValueError, ZeroDivisionError):
        pass

"""
Your code works, but it can be improved for clarity and efficiency. Here are some suggestions:
1. Simplify the logic for checking the conditions. You can combine some of the checks to make the code cleaner.
2. Use more descriptive variable names to enhance readability.
3. Avoid unnecessary conversions and calculations. For example, you can calculate the percentage directly without intermediate steps.
4. Consider using a function to encapsulate the logic for better organization and reusability.
5. Add comments to explain the purpose of each section of the code for better understanding.

- Use split("/", 1) instead of split("/", 2) (since you only expect one /).
- Only convert x and y to int once.
- Check for invalid input (like denominator = 0, negative numbers, or numerator > denominator) before doing calculations.
- Use more descriptive variable names.
"""

while True:
    try:
        fraction = input("Fraction: ")
        x_str, y_str = fraction.split("/", 1)
        x = int(x_str)
        y = int(y_str)

        if y == 0 or x < 0 or y < 0 or x > y:
            continue

        percent = round((x / y) * 100)

        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")
        break

    except (ValueError, ZeroDivisionError):
        pass


# taqueria

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")

        elif item not in menu:
            continue
        else:
            continue

    except EOFError:
        print("\n")
        break
    except KeyError:
        pass

# grocery

grocery_list = {}

while True:
    try:
        item = input().upper()

        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        print("\n")
        break
    except KeyError:
        pass

for item, quantity in sorted(grocery_list.items()):
    print(f"{quantity} {item}")

# outdated

# re needs to be imported at the top of the file


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").replace(",", "")

        separators = r"[/ ]"
        result = re.split(separators, date)
        # print(result)
        month, day, year = result

        if month.isalpha():
            if month.title() in months:
                month = months.index(month.title()) + 1
                # print(month)
            else:
                pass
        else:
            pass

        month = int(month)
        day = int(day)
        year = int(year)

    except ValueError:
        pass

    if month in range(1, 13):
        if day in range(1, 32):
            if year in range(0, 10000):
                print(f"{year}-{month:02}-{day:02}")
                break
