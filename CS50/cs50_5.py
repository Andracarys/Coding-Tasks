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
