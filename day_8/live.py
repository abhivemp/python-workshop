# ----------------------------
# Lesson 20: Reading and Writing Files
# ----------------------------

# ✅ BASIC FILE I/O

# You can open files using the open() function.
# Modes:
# - 'r' = read
        # File must exist
# - 'w' = write (overwrites existing file)
        # If the file exists, its contents will be truncated (emptied).
        # If the file does not exist, a new file will be created.
# - 'a' = append
        # If the file does not exist, a new file will be created.
# - 'r+' = read and write

# Writing to a file
'''
with open("day_8/example.txt", "w") as f:
    f.write("Yellow, class\n")
'''

'''open("day_8/example.txt", "w").close()'''

# Appending to a file
'''
with open("day_8/example.txt", "a") as file:
    file.write("Now Hello!\n")
'''
# Reading from a file
'''
with open("day_8/example.txt", "r") as file:
    file_content = file.read()
    print(file_content)
'''

# Reading line-by-line
'''
with open("day_8/example.txt", "r") as file:
    for i, each_line in enumerate(file):
        print(f"Line {i}: {each_line}" )
        
'''

'''
user_input = ""
while user_input != "exit":
    user_input = input("Input a number: ")

    with open("day_8/my_logs.txt", "a") as log_file:
        log_file.write(f"User input: {user_input}\n")
'''


'''
Revamp Your Calculators!!

Build a menu-driven calculator that performs arithmetic operations
and logs successful results to a history file.


1. Show menu:
   1) Calculate  2) View history  3) Clear history  4) Exit
2. Use functions for +, -, *, /
3. Log successful results to "history.txt" (e.g. 5 + 3 = 8)
4. View: read and print history.txt
5. Clear: wipe history.txt
6. Exit if user selects option 4
'''

# -----------------------------------
# ✅ WORKING WITH CSV / TSV FILES
# -----------------------------------

import csv
# CSV - Comma Separated File
# TSV - Tab Separated File
# Reading from a csv file
'''
with open("day_8/data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)
    for each_row in reader:
        print(f"Student Id: {each_row[0]}")
        # print(each_row)
    print("headers:", headers)
'''
'''
sum = 0
num = 0
with open("day_8/data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)
    for each_row in reader:
        num += 1
        sum += int(each_row[2])
        # print(f"Student Id: {each_row[0]}")
        # print(each_row)
    print("avg:", sum/num)
    '''


# Writing to a CSV file
'''
with open("day_8/data1.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([101,"Emily Carter",88,91])
'''
# Alternatively, using DictReader (reads headers automatically)
'''
sum = 0
num = 0
with open("day_8/data.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    print("Headers: ", reader.fieldnames)
    for each_row in reader:
        num += 1
        sum += int(each_row["Math"])
    print("avg:", sum/num)
'''
# Writing to a TSV file (tab-separated)

'''
with open("day_8/data1.tsv", "w") as tsv_file:
    writer = csv.writer(tsv_file, delimiter="\t")
    writer.writerow([101,"Emily Carter",88,91])
'''

# -----------------------------------
# ✅ WORKING WITH JSON FILES
# -----------------------------------

import json


# JSON (JavaScript Object Notation) is a lightweight format for storing and exchanging data.
# It's human-readable and widely used in web development and APIs.

# Though it comes from JavaScript, JSON is language-independent and supported by Python.

# ---------------------------------------
# 🧱 JSON Structure and Python Equivalents
# ---------------------------------------
# JSON Type     | Python Equivalent
# ------------- | ------------------
# Object        | dict
# Array         | list
# String        | str
# Number        | int or float
# Boolean       | True / False
# null          | None

# Example JSON data:
# {
#   "name": "Alice",
#   "age": 25,
#   "is_student": true,
#   "skills": ["Python", "HTML", "CSS"]
# }

# Python dictionary (can also be list, int, etc.)
person = {
    "name": "Aiden",
    "age": 17,
    "is_student": True,
    "skills": ["Python", "Data Analysis"]
}

# Writing JSON to a file
'''
with open("day_8/person.json", "w") as json_file:
    json.dump(person, json_file, indent=2)
'''
# Reading JSON from a file
'''
with open("day_8/person.json", "r") as json_file:
    json_person = json.load(json_file)
    print(json_person)
'''
# You can also convert between JSON and string
'''
json_string = json.dumps(person)
person_from_string = json.loads(json_string)
print("From String: ", person_from_string)
'''

# ----------------------------
# Lesson 21: Exception Handling
# ----------------------------

# ✅ TRY / EXCEPT / FINALLY

# Python uses try-except blocks to catch and handle errors.
'''
try:
    num = int(input("Enter a number: "))
    result = 25 / num
    print(result)
except ValueError:
    print("Thats not a number")
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("Thanks!")
'''

# https://docs.python.org/3/library/exceptions.html#bltin-exceptions

# ----------------------------
# Lesson 22: Custom Exceptions
# ----------------------------

# ✅ DEFINING CUSTOM EXCEPTIONS
'''
class NegativeNumberError(Exception):
    pass


def check_positive(n):
    if n < 0:
        raise NegativeNumberError()


try:
    num = int(input("Enter a number: "))
    check_positive(num)
    print("Your number was positive!")
    result = 25 / num
    print("Your result: ", result)
except NegativeNumberError:
    print("Please input a positive number")
except ValueError:
    print("Thats not a number")
except ZeroDivisionError:
    print("You cannot divide by zero")
'''

    



# You can create your own exceptions by subclassing Exception.

