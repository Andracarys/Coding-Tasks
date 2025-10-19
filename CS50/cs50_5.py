# Unit Tests
# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()


# from calculator1 import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()

# from calculator4 import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")


if __name__ == "__main__":
    main()

# from calculator5 import square


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

# from calculator6 import square


def test_positive():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


# import pytest
# from calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):  # expects a TypeError
        square("cat")  # should raise a TypeError when given a string input

# Has function return a str instead


def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()

# from hello1 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"

# from hello1 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

# twtter test


def main():
    word = input("Input: ")
    new_input = shorten(word)
    print("Output:", new_input)
    return new_input


def shorten(word):
    new_input = ""
    for char in word:
        if char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            continue
        else:
            new_input += char
    return new_input


if __name__ == "__main__":
    main()


# from twitter import shorten


def test_shorten():
    assert shorten("h") == "h"
    assert shorten("hi") == "h"
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("hEllO") == "hll"
    assert shorten("h3ll0") == "h3ll0"
    assert shorten("") == ""
    assert shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"
    assert shorten("BCDFGHJKLMNPQRSTVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"
    assert shorten(
        "The quick brown fox jumps over the lazy dog") == "Th qck brwn fx jmps vr th lzy dg"
    assert shorten("1234567890") == "1234567890"
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"
    assert shorten("This is a test!") == "Ths s  tst!"
    assert shorten("Python is fun") == "Pythn s fn"
    assert shorten("I love programming") == " lv prgrmmng"
    assert shorten("CS50 is awesome!") == "CS50 s wsm!"
    assert shorten("Let's remove vowels") == "Lt's rmv vwls"
    assert shorten("Aeiou are vowels") == " r vwls"
    assert shorten("This sentence has no vowels") == "Ths sntnc hs n vwls"
    assert shorten(
        "Why did the chicken cross the road?") == "Why dd th chckn crss th rd?"
    assert shorten(
        "Vowels are removed from this sentence.") == "Vwls r rmvd frm ths sntnc."
    assert shorten("End of tests.") == "nd f tsts."

#  Home Federal Savings Bank Test


def main():
    g = input("Write your greeting: ")
    print(value(g))


def value(greeting):
    greeting = greeting.strip().lower()

    hello = greeting.startswith("hello")
    h = greeting.startswith("h")

    if hello == True:
        return "$0"
    elif h == True:
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()

# from bank import value


def test_value_zero():
    assert value("hello") == "$0"
    assert value(" HELLO ") == "$0"


def test_value_twenty():
    assert value("hi") == "$20"
    assert value("hey") == "$20"


def test_value_hundred():
    assert value("GOOD MORNING") == "$100"
    assert value("") == "$100"
    assert value("1") == "$100"
    assert value("2") == "$100"
    assert value("3") == "$100"

# Re-requesting a Vanity Plate


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


if __name__ == "__main__":
    main()

# import plates


def test_valid_plates():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("AB123") == True
    assert plates.is_valid("HELLO1") == True
    assert plates.is_valid("A") == False
    assert plates.is_valid("BCD12A") == False
    assert plates.is_valid("12") == False
    assert plates.is_valid("BCD012") == False
    assert plates.is_valid("AS.%!") == False

# Refueling Test -- NOT FINISHED


def main():
    fraction = input("Fraction: ")
    percentage = gauge(fraction, convert(fraction))
    print(percentage)


def convert(fraction):
    while True:
        try:
            sectioning = fraction.split("/", 2)
            x, y = sectioning

            step_1 = int(x) / int(y)
            step_2 = round(step_1 * 100)
            return step_2

        except (ValueError, ZeroDivisionError):
            pass
        break


def gauge(fraction, percentage):
    sectioning = fraction.split("/", 2)
    x, y = sectioning

    while True:
        if int(x) > int(y):
            continue
        elif int(x) < 0 or int(y) < 0:
            continue
        elif percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            step_3 = str(percentage) + "%"
            return step_3

        break


if __name__ == "__main__":
    main()

# from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("2/3") == 67
    assert convert("5/5") == 100
    assert convert("0/5") == 0


def test_gauge():
    assert gauge("1/2", 50) == "50%"
    assert gauge("3/4", 75) == "75%"
    assert gauge("2/3", 67) == "67%"
    assert gauge("5/5", 100) == "F"
    assert gauge("0/5", 0) == "E"
    assert gauge("1/100", 1) == "E"
    assert gauge("99/100", 99) == "F"
