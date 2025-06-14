# ----------------------------
# Lesson 1: Variables, Data Types, and Basic Input/Output
# ----------------------------

# ✅ VARIABLES

# A variable is like a container that holds data.
# You assign values to variables using the = symbol.

'''
name = "Kevin"
name1 = "Abhi"

print(name1)
'''


# Strings are wrapped in quotes, numbers are not.
# Booleans are written as True or False (capitalized).

# Python is dynamically typed, so you can reassign a variable to a different type later.
# This is flexible, but can cause problems in large programs if not managed carefully.

# ✅ DATA TYPES

# Python has several built-in data types.
# Common ones include:
# - int (whole numbers)
# - float (decimal numbers)
# - str (text)
# - bool (True or False)
# - NoneType (represents 'no value')

name = "kevin" #str
name = 3 #int
name = 3.0 #float
name = True #bool
name = None #none
# print(name, type(name))

'''
Exercise 1: What data type should 
each of these variables be?

first_name = str
number_of_students = int
price_of_item = float
is_logged_in = bool
temperature = float
user_age = int
has_paid_subscription = bool
street_address = str
phone_number = str
total_score = float/int
average_grade = float
product_description = str
zip_code = str
'''
# zip_code = 08820
zip_code = int("08820")
# print(zip_code)


# You can check a variable's type using the `type()` function.

# ✅ BASIC OUTPUT

# We use the print() function to display output on the screen.
# You can print text, variables, or both together.

print("Hello, World!")

print("Hello,", "World!", "I am Here!")

w = "World!"
print("Hello", w, "I AM HERE!", sep="-")



p1 = "973"
p2 = "525"
p3 = "4577"

print()
# (973)-525-4577



# Strings can be combined with commas (which adds spaces),
# or with f-strings (which embed values directly inside the text).

# Customizing the Separator and Ending

# Formatting basics

# ✅ BASIC INPUT

# The input() function lets you collect information from the user.
# It always returns a string, no matter what the user types.
# If you want to work with numbers, you need to convert the input using int() or float().
number = input("Enter your favorite number: ")
number = None
# float(number)
# int(number)
# str(number)
print(number, type(number))

# Always explain that improper input (like typing a letter when expecting a number)
# will cause an error — we’ll handle that later when we learn error handling.

# You can use simple logic to interpret responses — like turning 'yes' into True.

# ✅ WRAP-UP

# Today, we learned:
# - How to create and reassign variables
# - The core data types in Python
# - How to print and collect input
# - How type conversion works

# These are the building blocks we’ll build on next session with logic and control flow.
