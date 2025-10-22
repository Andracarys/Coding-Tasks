# File I/O in Python

# Writes to a file

from PIL import Image
import sys
name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()

# Appends to a file

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# Adds context manager

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# Reads from a file

with open("names.txt") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

# rstrip()  # removes trailing whitespace characters like \n
# or use strip() to remove leading and trailing whitespace
# or use lstrip() to remove leading whitespace only
# rm names.txt  # command to remove the file from terminal

# Reads from a file, one line at a time

with open("names.txt") as file:
    for line in file:
        print("hello,", line.rstrip())

# Reads from a file, sorting lines

with open("names.txt") as file:
    for line in sorted(file):  # sorts lines while reading
        print("hello,", line.rstrip())

# Reads from a file, sorting lines in reverse order

with open("names.txt") as file:
    # sorts lines in reverse order while reading
    for line in sorted(file, reverse=True):
        print("hello,", line.rstrip())

# Appends names to a list for sorting

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

# "r"  # read mode is default
# "w"  # write mode (overwrites existing file or creates new file)
# "a"  # append mode (creates new file if none exists)
# "x"  # exclusive creation mode (creates new file, errors if file exists)
# "b"  # binary mode (for non-text files)
# "t"  # text mode (default mode for text files)

# sorted()  # returns a new sorted list from the iterable
# sort()    # sorts the list in place
# names.sort()  # alternative way to sort the list in place
# names.reverse()  # reverses the list in place
# names.append("new_name")  # adds a new name to the end of the list
# names.remove("name")  # removes the first occurrence of the name from the list
# names.pop()  # removes and returns the last item from the list
# names.clear()  # removes all items from the list
# names.index("name")  # returns the index of the first occurrence of the name
# names.count("name")  # returns the number of occurrences of the name in the list
# len(names)  # returns the number of items in the list
# names.insert(index, "name")  # inserts a name at the specified index
# names.extend(["name1", "name2"])  # extends the list by appending elements from another iterable
# names.copy()  # returns a shallow copy of the list
# for name in names:  # iterates over each name in the list

# Reads a CSV file

with open("students0.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# split(",")  # splits a string into a list at each comma
# join()      # joins a list into a string with a specified separator
# row[0]     # accesses the first element of the list

# Unpacks a list

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

# Sorts a list of strings

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

# Reads a CSV file into a list of dict objects, creating empty dict first

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

# Reads a CSV file into a list of dict objects, creating dict first 😎😎😎

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

# Reads a CSV file into a list of dict objects

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for student in students:
    print(f"{student['name']} is in {student['house']}")

# dict()  # creates a new dictionary
# student["key"] = value  # adds a key-value pair to the dictionary
# student["key"]  # accesses the value associated with the key
# student.get("key")  # accesses the value associated with the key, returns None if key not found
# student.keys()  # returns a view of the dictionary's keys
# student.values()  # returns a view of the dictionary's values
# student.items()  # returns a view of the dictionary's key-value pairs
# for key in student:  # iterates over each key in the dictionary
# for key, value in student.items():  # iterates over each key-value pair in the dictionary
# len(student)  # returns the number of key-value pairs in the dictionary
# del student["key"]  # removes the key-value pair from the dictionary
# student.clear()  # removes all key-value pairs from the dictionary

# Sorts a list of dictionaries using a function

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})


def get_name(student):
    return student["name"]


def get_house(student):
    return student["house"]  # not used but here for reference


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

# Sorts a list of dictionaries using a lambda function

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

# lambda parameter: expression  # creates an anonymous function
# sorted(iterable, key=function)  # sorts the iterable using the function to extract a sort key
# key=lambda student: student["name"]  # sorts by the "name" key in the dictionary
# key=lambda student: student["house"]  # sorts by the "house" key in the dictionary
# for student in sorted(students, key=lambda student: student["name"]):  # iterates over sorted list
# students.sort(key=lambda student: student["name"])  # sorts the list in place by "name" key
# students.sort(key=lambda student: student["house"])  # sorts the list in place by "house" key
# for student in students:  #iterates over unsorted list

# Reads a CSV file using csv.reader

# import csv

students = []

with open("students1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# Reads a CSV file using csv.reader with unpacking

students = []

with open("students1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# csv.reader(file)  # creates a reader object that iterates over lines in the CSV file
# row[0]  # accesses the first column in the row
# row[1]  # accesses the second column in the row
# name, home = row  # unpacks the row into name and home variables
# for row in reader:  # iterates over each row in the CSV file
# for name, home in reader:  # iterates over each row with unpacking

# Reads a CSV file using csv.DictReader

# import csv

students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# csv.DictReader(file)  # creates a DictReader object that maps the information in each row to a dict
# row["name"]  # accesses the value associated with the "name" key in the row dictionary
# row["home"]  # accesses the value associated with the "home" key in the row dictionary
# for row in reader:  # iterates over each row in the CSV file

# Writes a CSV file using csv.writer

# import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

# csv.writer(file)  # creates a writer object that writes to the CSV file
# writer.writerow([value1, value2])  # writes a row to the CSV file
# writerows([[value1, value2], [value3, value4]])  # writes multiple rows to the CSV file

# Writes a CSV file using csv.DictWriter

# import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a") as file:
    # fieldnames defines the order of columns
    # creates a DictWriter object that writes to the CSV file
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

# csv.DictWriter(file, fieldnames=keys)  # creates a DictWriter object that writes to the CSV file
# writer.writerow({"key1": value1, "key2": value2})  # writes a row to the CSV file using a dict
# writer.writerows([{"key1": value1, "key2": value2}, {"key1": value3, "key2": value4}])  # writes multiple rows to the CSV file using a list of dictionaries
# writer.writeheader()  # writes the header row to the CSV file using the fieldnames
# fieldnames=["name", "home"]  # defines the order of columns in the CSV file

# Opens and saves binary files

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

# PIL.Image.open(file)  # opens and identifies the given image file
# image.save(file, options)  # saves the image to the given file with options
# save_all=True  # saves all frames of an image (for animated images)
# append_images=[image1, image2]  # appends additional images to the saved file
# duration=milliseconds  # sets the duration between frames in an animated image
# loop=0  # sets the number of loops for an animated image (0 means infinite)
# sys.argv  # list of command-line arguments passed to the script

# sys.argv[1:]  # list of command-line arguments excluding the script name
# for arg in sys.argv[1:]:  # iterates over each command-line argument
# images.append(image)  # adds the image to the images list
# images[0]  # accesses the first image in the images list
# images[1]  # accesses the second image in the images list

# To run this script, use the command:
# python cs50_6.py costume1.png costume2.png
# Make sure to have the images costume1.png and costume2.png in the same directory as the script.
# The output will be an animated GIF named costumes.gif created from the input images.

# Note: You need to have the Pillow library installed to run this script.
# You can install it using pip:
# pip install Pillow

# Pillow

# Pillow is a Python Imaging Library (PIL) fork that adds support for opening, manipulating,
# and saving many different image file formats.
# It is widely used for image processing tasks in Python.
# Official documentation: https://pillow.readthedocs.io/en/stable/
# Installation: pip install Pillow
# Basic usage:
# from PIL import Image
# image = Image.open("example.jpg")  # Open an image file
# image.show()  # Display the image
# image.save("example.png")  # Save the image in a different format
# image.resize((width, height))  # Resize the image
# image.rotate(angle)  # Rotate the image by a given angle
# image.crop((left, upper, right, lower))  # Crop the image to the specified box
# image.convert("L")  # Convert the image to grayscale
# image.filter(ImageFilter.BLUR)  # Apply a blur filter to the image
# image.format  # Get the format of the image (e.g., JPEG, PNG)
# image.size  # Get the size of the image (width, height)
# image.mode  # Get the color mode of the image (e.g., RGB, RGBA, L)
# More advanced features include drawing shapes, adding text, and working with image sequences (e.g., animated GIFs).
# Example of creating an animated GIF from multiple images:
# images = [Image.open("frame1.png"), Image.open("frame2.png")]
# images[0].save("animation.gif", save_all=True, append_images=images[1:], duration=200, loop=0)

# from PIL import Image


def main():
    img = Image.open("in.jpeg")
    img.close()


main()

# from PIL import Image


def main():
    with Image.open("in.jpeg") as img:
        print(img.size)
        print(img.format)


main()

# Image.size  # returns a tuple (width, height) of the image
# Image.format  # returns the format of the image (e.g., JPEG, PNG)
# Image.close()  # closes the image file
# with Image.open("in.jpeg") as img:  # context manager to open and
# automatically close the image file
# print(img.size)  # prints the size of the image

# from PIL import Image


def main():
    img = Image.open("in.jpeg")
    print(img.size)
    print(img.format)
    img.close()


main()

# from PIL import Image


def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img.save("out.jpeg")


main()

# Image.rotate(angle)  # rotates the image by the given angle (in degrees)
# Image.save(file)  # saves the image to the specified file
# img = img.rotate(180)  # rotates the image by 180 degrees
# img.save("out.jpeg")  # saves the rotated image as out.jpeg

# from PIL import Image
# from PIL import ImageFilter


def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.BLUR)
        img.save("out.jpeg")


main()

# Image.filter(filter)  # applies the given filter to the image
# ImageFilter.BLUR  # a predefined blur filter
# img = img.filter(ImageFilter.BLUR)  # applies a blur filter to the image

# from PIL import Image
# from PIL import ImageFilter


def main():
    with Image.open("/Users/andracarys/Desktop/Essentials/coding/CS50/Images/in.jpeg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")


main()

# ImageFilter.FIND_EDGES  # a predefined filter that finds edges in the image
# img = img.filter(ImageFilter.FIND_EDGES)  # applies the find edges filter to the image

# Reading and Writing CSV Files with the csv Module

# import csv
# import numpy as np
# from PIL import Image


def main():
    with open("views.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()

# csv.DictReader(file)  # creates a DictReader object that maps information in each row to a dict
# row["key"]  # accesses the value associated with the key in the row dictionary
# Image.convert("L")  # converts the image to grayscale
# np.array(image)  # converts the image to a NumPy array
# np.mean(array)  # calculates the mean of the array elements
# brightness = np.mean(np.array(image.convert("L"))) / 255  # calculates normalized brightness

# To run this script, ensure you have the required CSV file and image files in the same directory.
# The script reads the CSV file and prints each row as a dictionary.
# It also defines a function to calculate the brightness of an image using the Pillow and NumPy libraries.
# Make sure to have the Pillow and NumPy libraries installed to run this script.
# You can install them using pip:
# pip install Pillow numpy
# Note: The calculate_brightness function is defined but not called in this script.

# import csv
# import numpy as np
# from PIL import Image


def main():
    with open("views.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            print(round(brightness, 2))


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()

# round(value, 2)  # rounds the value to 2 decimal places
# brightness = calculate_brightness(f"{row['id']}.jpeg")  # calculates brightness for the image with the given id
# f"{row['id']}.jpeg"  # constructs the filename using the id from the CSV row
# The script reads the CSV file, calculates the brightness of each image based on the id in the CSV,
# and prints the rounded brightness value for each image.
# Note: The image files should be named according to the ids in the CSV file (e.g., 1.jpeg, 2.jpeg, etc.).

# import csv
# import numpy as np
# from PIL import Image


def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(
            analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()  # write header to analysis.csv

        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            print(round(brightness, 2))


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()

# csv.DictWriter(file, fieldnames=keys)  # creates a DictWriter object that writes to the CSV file
# writer.writeheader()  # writes the header row to the CSV file using the fieldnames
# fieldnames=reader.fieldnames + ["brightness"]  # adds "brightness" to the existing fieldnames from the reader
# The script reads the views.csv file, calculates the brightness of each image based on the id in the CSV,
# and writes the results to a new analysis.csv file with an additional "brightness" column.
# Note: The image files should be named according to the ids in the CSV file (e.g., 1.jpeg, 2.jpeg, etc.).

# import csv
# import numpy as np
# from PIL import Image


def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(
            analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            writer.writerow(
                {
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2),
                }
            )


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()

# writer.writerow({"key1": value1, "key2": value2})  # writes a row to the CSV file using a dict
# The script reads the views.csv file, calculates the brightness of each image based on the id in the CSV,
# and writes the results to a new analysis.csv file with an additional "brightness" column.
# Each row in analysis.csv contains the id, english_title, japanese_title, and brightness rounded to 2 decimal places.
# Note: The image files should be named according to the ids in the CSV file (e.g., 1.jpeg, 2.jpeg, etc.).

# import csv
# import numpy as np
# from PIL import Image


def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(
            analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = round(
                calculate_brightness(f"{row['id']}.jpeg"), 2)
            writer.writerow(row)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()

# row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"), 2)  # adds brightness to the row dictionary
# writer.writerow(row)  # writes the updated row dictionary to the CSV file

# Reading and Writing files


def main():
    with open("alice.txt", "r") as f:
        # contents = f.read() # reads the entire file as a single string
        contents = f.readlines()

    chapter1 = contents[52:272]
    with open("chapter1.txt", "w") as f:
        # f.write("Chapter I") # writes a single string to the file
        f.writelines(chapter1)  # writes a list of strings to the file


main()

# readlines()  # reads all lines from the file and returns a list of lines
# writelines(list_of_lines)  # writes a list of lines to the file
# contents[52:272]  # slices the list to get lines from index 52 to 271 (272 is exclusive)
# The script reads the contents of alice.txt, extracts lines corresponding to chapter 1,
# and writes those lines to a new file named chapter1.txt.
# Note: The line indices (52 to 272) are based on the specific structure of alice.txt
# and may vary for different texts.
# Make sure alice.txt is in the same directory as the script when running it.
# To run this script, ensure you have the alice.txt file in the same directory.
# The output will be a new file named chapter1.txt containing the extracted lines.
