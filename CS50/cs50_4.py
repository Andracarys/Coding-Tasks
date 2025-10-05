# Libraries

# Demonstrates import and random.choice

import inflect
from pyfiglet import Figlet
import emoji
import requests
import sys
import random

coin = random.choice(["heads", "tails"])
print(coin)

# Demonstrates from: from random import choice

coin = choice(["heads", "tails"])
print(coin)

# Demonstrates randint from: import random

number = random.randint(1, 10)
print(number)

# Demonstrates shuffle: import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

# Demonstrates statistics: import statistics

print(statistics.mean([100, 90]))
print(statistics.median([100, 90, 80]))
print(statistics.stdev([100, 90, 80]))
print(statistics.variance([100, 90, 80]))
print(statistics.mode([100, 90, 80, 90]))
print(statistics.harmonic_mean([100, 90, 80]))
print(statistics.geometric_mean([100, 90, 80]))
print(statistics.quantiles([100, 90, 80, 70, 60], n=4))
print(statistics.fmean([100, 90, 80]))
print(statistics.pstdev([100, 90, 80]))
print(statistics.pvariance([100, 90, 80]))
print(statistics.correlation([100, 90, 80], [30, 20, 10]))
print(statistics.covariance([100, 90, 80], [30, 20, 10]))
print(statistics.NormalDist(mu=0, sigma=1).pdf(1))
print(statistics.NormalDist(mu=0, sigma=1).cdf(1))

# Demonstrates sys.argv: import sys

print("hello, my name is", sys.argv[1])

# Adds error checking: import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

# Demonstrates sys.exit: import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

# Demonstrates list slice: import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# Demonstrates pip-installed package: import cowsay, import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

# Demonstrates a t-rex: import cowsay, import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])

# Demonstrates requests: import sys, import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(response.json())

# Demonstrates json: import json, import sys, import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(json.dumps(response.json(), indent=2))

# Demonstrates iterating over JSON: import json, import sys, import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
o = response.json()
for result in o["results"]:
    print(result["trackName"])

# Check __name__


def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


if __name__ == "__main__":  # used to prevent code from being run when imported
    main()

# Demonstrates own module: import sys, from sayings2 import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

# APIs: import requests


def main():
    response = requests.get("https://api.artic.edu/api/v1/artworks/search")
    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()

# : import sys, import requests


def main():
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search")
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        sys.exit(1)  # return

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()

# : import sys, import requests


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist, "limit": 3})
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        sys.exit(1)

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()

# Problem 4 Homework
# Emojize: import emoji


msg = input("Input: ")
if msg == ":thumbsup:":
    msg = ":thumbs_up:"
elif msg == "hello, :earth_asia:":
    msg = "hello, :globe_showing_Asia-Australia:"

emojized = emoji.emojize(msg)
print(f"Output: {emojized}")

# FIGlet: import sys, import random, from pyfiglet import Figlet

figlet = Figlet()

all_fonts = figlet.getFonts()
random_font = random.choice(all_fonts)

if len(sys.argv) == 1:
    figlet.setFont(font=random_font)

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    if sys.argv[2] in all_fonts:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid font")
else:
    sys.exit("Usage: python try.py [-f FONTNAME]")

message = input("Input: ")
print(figlet.renderText(message))

# Adieu: install inflect package via pip and import inflect


people = []
p = inflect.engine()

while True:
    try:
        user_input = input("Name: ")
        people.append(user_input)
    except EOFError:
        print()
        break

join = p.join(people)
print(f"Adieu, adieu, to {join}")

# Guessing Game: import random

while True:
    level = input("Level: ")

    if level.isnumeric() is False:
        continue
    elif int(level) < 1 or int(level) > 10:
        continue
    else:
        break

random_number = random.randint(1, 101)

while True:

    guess = input("Guess: ")

    if guess.isnumeric() is False:
        continue
    elif int(guess) < 1:
        continue
    elif int(guess) < random_number:
        print("Too small!")
    elif int(guess) > random_number:
        print("Too large!")
    else:
        print("Just right!")
        break

# Little professor: import random


def main():
    level = get_level()
    questions = 0
    score = 0
    answer_counter = 0  # number of tries per question, incorrect answers

    while questions < 10:
        try:
            x, y = generate_integer(level)
            answer = int(input(f"{x} + {y} = "))
        except ValueError:
            answer_counter += 1
            print("EEE")
        else:
            if answer == x + y:
                score += 1
                answer_counter = 0
                questions += 1
            else:
                print("EEE")
                answer_counter += 1
            if answer_counter == 3:
                print(f"{x} + {y} = {x + y}")
                answer_counter = 0
                questions += 1
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
            return level
        except ValueError:
            continue


def generate_integer(level):
    try:
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        return x, y
    except ValueError as exc:
        if level not in [1, 2, 3]:
            raise ValueError("Level must be 1, 2, or 3") from exc


if __name__ == "__main__":
    main()


# bitcoin: import sys, import requests

# Expects the user to specify as a command-line argument
# the number of Bitcoins: 𝑛, that they would like to buy.
# If that argument cannot be converted to a float,
# the program should exit via sys.exit with an error message.
# Queries the API for the CoinCap Bitcoin Price Index
# at rest.coincap.io/v3/assets/bitcoin?apiKey = YourApiKey.
# You should replace YourApiKey with the actual API key you obtained
# from your CoinCap account dashboard, which returns a JSON object,
# among whose nested keys is the current price of Bitcoin as a float.
# Be sure to catch any exceptions.
# Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places,
# using , as a thousands separator.

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    n = float(sys.argv[1])
    if n < 0:
        sys.exit("Command-line argument must be a positive number")
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=bd7d4b92fcd5e5b7ec00f8b461a3eb324ce133f3f34cbc350d8cdc39fdb27fe3",
        timeout=10)  # timeout added to avoid hanging indefinitely
    response.raise_for_status()
    bitcoin_data = response.json()
    price = float(bitcoin_data["data"]["priceUsd"])
    cost = n * price
    print(f"${cost:,.4f}")
except requests.RequestException:
    sys.exit("Network error")
