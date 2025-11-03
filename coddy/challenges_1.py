# Coddy: Section 2: Challenges

student_records = {}


def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
        return
    student_records[name] = {
        "age": age, "grades": set(), "courses": set(courses)
    }
    print(f"Student '{name}' added successfully.")


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
print(student_records)

###

result = sum(range(1, 6), 5)
print(result)

###

numbers = [42, 17, 23, 56, 9, 34]
words = ["kiwi", "apple", "banana", "cherry", "date"]
minnum = min(numbers)
maxnum = max(numbers)
minword = min(words)
maxword = max(words)
print("Smallest number:", minnum)
print("Largest number:", maxnum)
print("Smallest word:", minword)
print("Largest word:", maxword)

###

temperatures = [72, 68, 75, 80, 65, 70, 78]
humidity = [60, 55, 65, 70, 50, 58, 62]
mintemp = min(temperatures)
maxtemp = max(temperatures)
minhum = min(humidity)
maxhum = max(humidity)
print("Highest Temperature:", maxtemp)
print("Lowest Temperature:", mintemp)
print("Highest Humidity:", maxhum)
print("Lowest Humidity:", minhum)

###


def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return
    student_records[name]["grades"].add(grade)
    print("Grade {grade} added for student '{name}'.")


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(student_records)

###


def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    if not student_records[name]["grades"]:
        return 0
    else:
        average = float(
            ((sum(student_records[name]["grades"])) / len(student_records[name]["grades"])))
        return average


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
print(calculate_average_grade("Alice"))  # Should return 87.5
print(calculate_average_grade("Bob"))  # Should return 75.0
# Non-existent student, should print message and return None
print(calculate_average_grade("Charlie"))
print(calculate_average_grade("Alice"))  # Should return 87.5 again

###


def list_students_by_course(course):
    courselist = []
    for name, details in student_records.items():
        if course in details["courses"]:
            courselist.append(name)
    return courselist


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list

###


def filter_top_students(threshold):
    topst = []
    for name, details in student_records.items():
        average = calculate_average_grade(name)
        if average > threshold:
            topst.append(name)
    return topst


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list

###

dicts = {'a': 3, 'b': 1, 'c': 2}


def dictionary_sorter(data_dict):
    items = list(data_dict.items())

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] > items[j][1]:  # Compare values
                # Swap if out of order: x,y = y,x == #1,#2 = #2,#1
                items[i], items[j] = items[j], items[i]

    sorteddict = {}
    for key, value in items:
        sorteddict[key] = value
    return sorteddict


print(dictionary_sorter(dicts))

###


def analyze_grades(grades):
    # Calculate the average grade
    # Use grades.values() to get the actual grades
    average = sum(grades.values()) / len(grades)

    # Find the highest grade
    high = max(grades.values())  # Find max from the values of the grades dict

    # Find the lowest grade
    low = min(grades.values())  # Find min from the values of the grades dict

    # Print students with the highest and lowest grades
    top_student = [name for name,
                   grade in grades.items() if grade == high][0]
    bottom_student = [name for name,
                      grade in grades.items() if grade == low][0]

    # Return the results as a dictionary
    return {
        'average': round(average, 2),
        'highest': high,
        'lowest': low,
        'top_student': top_student,
        'bottom_student': bottom_student
    }


# Test the function
student_grades = {'Alice': 85, 'Bob': 92,
                  'Charlie': 78, 'David': 95, 'Eve': 88}
# Call the function with student_grades
result = analyze_grades(student_grades)
print(result)  # This will print None because the function does not return a value

"""
    Print students with the highest and lowest grades
    for name, grade in grades.items():
        if grade == low:  # Check if the grade is the lowest
            print(name)
        if grade == high:  # Check if the grade is the highest
            print(name)
"""

###


def house_of_lists(list_of_lists):
    filterout = [list_of_lists.remove(
        lst) for lst in list_of_lists if sum(lst) > 50]
    extract = [num for lst in list_of_lists for num in lst if num < 5]
    return extract


nested = [[1, 2], [3, 4], [52, 60]]
print(house_of_lists(nested))

###
inventory = {}


def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
        return
    else:
        try:
            inventory[item] = {"price": float(price), "stock": int(stock)}
            print(f"Item '{item}' added successfully.")
        except ValueError:
            print("Error: Price and stock must be numeric.")


add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
print(inventory)


def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
        return
    try:
        newstock = inventory[item]["stock"] + int(quantity)
        if newstock < 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] = newstock
            print(f"Stock for '{item}' updated successfully.")
    except ValueError:
        print("Error: Quantity must be an integer.")


add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
update_stock("Apple", -20)
update_stock("Banana", 30)
update_stock("Orange", 10)  # Should print an error
update_stock("Apple", -90)
print(inventory)


def check_availability(item):
    if item not in inventory:
        return "Item not found"
    else:
        return inventory[item]["stock"]


add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found"


def sales_report(sales):
    totalrevenue = 0
    for item, quantity in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue
        if inventory[item]["stock"] < quantity:
            print(f"Error: Insufficient stock for '{item}'.")
            continue
        inventory[item]["stock"] -= quantity
        totalrevenue += quantity * inventory[item]["price"]
    return f"Total revenue: ${totalrevenue:.2f}"


add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
# Orange should print an error
sales = {"Apple": 30, "Banana": 20, "Orange": 10}
print(sales_report(sales))  # Should output: 19.0
print(inventory)

###
