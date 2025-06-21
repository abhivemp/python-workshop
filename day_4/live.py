# ----------------------------
# Lesson 6: if, elif, else Statements
# ----------------------------

# If Statement Structure
# if (conditional):
#     do something here
# else: # optional
#     do something here instead
# Conditions

# age = 18

# if age < 13:
#     print("you are a child")
# elif age < 18:
#     print("You are a teenager")
# else:
#     print("Youre an adult!")

# Statements

# temperature = 70

# if temperature > 60 and temperature < 80:
#     print("This is hella nice weather")
# else:
#     print("it's either too hot or too cold")

# where a certain variable has a value or not I can use this

# isNotEmpty = ""

# if isNotEmpty:
#     print("It's not empty at all")
# else:
#     print("Please input the variable.")

# The Super simple calculator
# Write a program that acts like a simple calculator. It should:
# Ask the user to input two numbers.
# Ask the user to choose an operation: +, -, *, or /.
#   Handle division by zero with a friendly error message.
# Perform the operation and display the result.

# Enter the first number: 10  
# Enter the second number: 2  
# Choose an operation (+, -, *, /): /  
# Result: 5.0
# Enter the first number: 6  
# Enter the second number: 2  
# Choose an operation (+, -, *, /): +  
# Result: 8.0
# Enter the first number: 10  
# Enter the second number: 1  
# Choose an operation (+, -, *, /): *  
# Result: 10.0


'''
while(True):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose an operation (+, -, , /): ")

    if operator == "+":
        result = num1 + num2
        print(num1 + num2)

    if operator == "-":
        result = num1 - num2
        print(num1 - num2)
        if (num1 == 100 and num2 == 50):
            break

    if operator == "":
        result = num1 * num2
        print(num1 * num2)

    if operator == "/":
        if num2 == 0:
            print("Sorry, dividing by 0 is undefined :(")
            result = 0.0
        else:
            result = num1 / num2
            print(num1 / num2)
    
    if result == 10 :
        break
    
'''

# Tax Brackets

# Write a program that asks the user to enter their annual income, and calculates how much 
# federal income tax they owe based on U.S. tax brackets.

# Use these 2023 (single filer) tax brackets for reference:

# Income Bracket        Tax Rate
# $0 - $11,000            10%
# $11,001 - $44,725        12%
# $44,726 - $95,375        22%
# $95,376 - $182,100    24%
# $182,101 - $231,250    32%
# $231,251 - $578,125    35%
# $578,126 and above    37%

# Should calculate the progressive tax amount
# Ask until the user enters "exit"

# ------------------------------
# Enter your annual income: $50000
# You owe: $6,308.50 in federal income tax.
# Enter your annual income: exit
# Thank you for using the OG Tax Calculator


# ----------------------------
# Lesson 8: Loops (for and while)
# ----------------------------

# For Loop Structure
'''
for item in sequence:
    loop body
    
'''

'''
x = [1,2,3,4,5,6,7]

for num in x:
    print(num)

for index, num in enumerate(x):
    print (index, num)

'''

# While Loop Structure

'''
while(condition):
    loop body 
    loop break statement/condition update
'''
'''
x = [1,2,3,4,5,6,7]
num = 0
while(num < 5):
    print(x)
    num = num+1
    
'''


'''
iterations = 10
start = 0
while(start < iterations):
    print("x"*start)
    start = start+1
    
'''

# Loop Keywords
# `break`
# `continue`

'''
iterations = 10
start = 0
while(start < iterations):
    print("x"*start)
    if start == 6:
        break
    start = start+1
    
'''


'''
iterations = 10
start = 0
while(start < iterations):
    if start == 6:
        start = start +1
        continue
    print("x"*start)
    start = start+1
    
'''

'''
x = [1,2,3,4,5,6,7]
for num in x:
    if num == 6:
        continue
    print("x"*num)
    
'''

'''
x = [1,2,3,4,5,6,7,8,9]
for num in x:
    print("for:", num)
    
'''

'''
index = 0
while(index < len(x)):
    print("while", x[index])
    index = index + 1
    
'''





'''
word = "hello"
while(True):
    guess = input("Guess a word - if its right, you win: ")
    if guess == word:
        break
    
'''
