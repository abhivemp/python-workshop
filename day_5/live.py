## Tax Brackets

# Write a program that asks the user to enter their annual income, and calculates how much 
# federal income tax they owe based on U.S. tax brackets.

# Use these 2023 (single filer) tax brackets for reference:
# Income Bracket	    Tax Rate
# $0 - $11,000	        10%
# $11,001 - $44,725	    12%
# $44,726 - $95,375	    22%
# $95,376 - $182,100	24%
# $182,101 - $231,250	32%
# $231,251 - $578,125	35%
# $578,126 and above	37%

# Should calculate the progressive tax amount
# Ask until the user enters "exit"

# ------------------------------
# Enter your annual income: $50000
# You owe: $6,307.50 in federal income tax.
# Enter your annual income: exit
# Thank you for using the OG Tax Calculator

'''
while True:
    user_input = input("Enter your annual income: $")
    if user_input == "exit":
        break

    annual_income = float(user_input)
    tax = 0.0

    if annual_income > 578125:
        tax += (annual_income - 578125) * 0.37
        annual_income = 578125
    if annual_income > 231250:
        tax += (annual_income - 231250) * 0.35
        annual_income = 231250
    if annual_income > 182100:
        tax += (annual_income - 182100) * 0.32
        annual_income = 182100
    if annual_income > 95375:
        tax += (annual_income - 95375) * 0.24
        annual_income = 95375
    if annual_income > 44725:
        tax += (annual_income - 44725) * .22
        annual_income = 44725
    if annual_income > 11000:
        tax += (annual_income - 11000) * .12
        annual_income = 11000
    if annual_income > 0:
        tax += annual_income * .10
        annual_income = 44725

    print(f"You owe: ${tax:,.2f} in federal income tax.")
'''



#  1. List
fruits = ["apple", "banana", "cherry", "date", "mango"]
# Write a loop to print each fruit on a new line

#  2. Tuple
colors = ("red", "green", "blue")
# Write a loop to print each color with the text: "Color: <color>"

# 3. Dictionary
student_grades = {
    "Alice": 90,
    "Bob": 95,
    "Charlie": 98
}
# Write a loop to print each student's name and grade in the format: "<name> got <grade>"
'''
print(student_grades.keys())

keys = student_grades.keys()
for key in keys:
    print(f"{key} got {student_grades[key]}")

print(student_grades.values())

print(student_grades.items())
items = student_grades.items()
for item in items:
    print(f"{item[0]} got {item[1]}")

# tuple unpacking
for student_name, grade in student_grades.items():
    print(f"{student_name} got {grade}")

for key, value in student_grades.items():
    print(f"{key} got {value}")
'''

#  4. Set
unique_numbers = {3, 7, 2, 5}
# Write a loop to print each number with the text: "Number: <number>"



# ----------------------------
# Lesson 10: Writing Functions
# ----------------------------

# print("the function")
# len(unique_numbers)

# Function Definition Structure

'''
def <name>():
    function body
'''

def print_name():
    print("Kevin")

'''
print_name()
'''

# Parameters
'''
def <name>(parameters):
    function body

<name>(arguments)
'''

def print_any_name(name):
    print(name)

'''
print_any_name("Kevin")
print_any_name("Abhi")
'''

# Return Types
'''
def <name>(parameters):
    function body
    return statement

return_value = <name>(arguments)
'''

def add_numbers(num1, num2):
    result = num1 + num2
    return result

'''
s1 = add_numbers(3,4)
print(s1)
s2 = add_numbers(5,6)
print(s2)
print(add_numbers(7,8))
'''

# The Super simple calculator
# Write a program that acts like a simple calculator. It should:
# Ask the user to input two numbers.
# Ask the user to choose an operation: +, -, *, or /.
#   Handle division by zero with a friendly error message.
# Perform the operation and display the result.
# Write new functions for each of the operators and call them
# to evaluate the answer

# Enter the first number: 10  
# Enter the second number: 2  
# Choose an operation (+, -, *, /): /  
# Result: 5.0

'''
while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    operation = input("Choose an operation (+, -, *, /): ")


    if operation == "+":
        result = num1 + num2
        print("Result:", result)

    elif operation == "-":
        result = num1 - num2
        print("Result:", result)

    elif operation == "*":
        result = num1 * num2
        print("Result:", result)

    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)
    
    if result == 10 :
        break

else:
    print("Invalid operation. Please choose +, -, *, or /.")
'''

# Default Parameters

def welcome(name="Abhi"):
    print("Welcome,", name)

'''
welcome()
welcome("Kevin")
'''


# Keyword Arguments

def describe_pet(animal, name):
    print(f"{name} is a {animal}")

'''
describe_pet(name="Po", animal="Panda")
'''





















# ----------------------------
# Lesson 11: Importing and Using Modules
# ----------------------------

# Importing Module Structures

import math

'''print("sqr root 16: ", math.sqrt(16))'''

from math import sqrt, pi 

'''
print("sqr root 16: ", sqrt(16))
print("pi: ", pi)
'''

import random

#float 0.0 1.0
'''print(random.random())'''

# integer between a and b (inclusive)
'''print(random.randint(1, 10))'''

# returns a random integer from the specified range
'''print(random.randrange(6,100,10))'''

fruits = ["apple", "banana", "cherry", "date", "mango"]

# single item
'''print(random.choice(fruits))'''

'''print(fruits[random.randint(0, len(fruits)-1)])'''


# with replacement
'''print(random.choices(fruits, k=3))'''
# without replacement
'''print(random.sample(fruits, k=3))'''
