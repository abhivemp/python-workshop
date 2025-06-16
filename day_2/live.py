# ----------------------------
# Lesson 2: Arithmetic, Comparison, and Logical Operators
# ----------------------------

# ✅ ARITHMETIC OPERATORS

# In python we have 7 basic operators for handling
# simple arithmetic

# Python follows standard order of operations but 
# common practice for readability is to use parentheses


# Addition (+)

# Subtraction (-)

# Multiplication (*)

# Division (/)

# Floor Division (//)

# Modulus (%)

# Exponentiation (**)



# ✅ COMPARISON OPERATORS

# We also have standard comparison operators in python


# Equal (==)

# Not equal (!=)

# Greater than (>)

# Less than (<)

# Greater than or equal (>=)

# Less than or equal (<=)



# ✅ LOGICAL OPERATORS

# Lastly are the Logical Operators 

# and

# or

# not



# ----------------------------
# Lesson 3: Strings and String Manipulation
# ----------------------------

# ✅ STRING BASICS

# String manipulation is one of the most fundamental 
# topics to master.

### different quote types

# Single and Double 
x = "hello"
x = 'hel"lo'
# Multi-Line
x = '''hel

ooo'''

### Repetition 

# Concatenating Strings
x = "hello"
y = "world"
z = x + y #helloworld

z = "hello""world"
# Multiplying strings
z = "kevin" * 3
# print(z)

## Escape Characters

# k = "My name \nis "Kevin""
# print(k,sep="", end="")

# print()





# name = 
"kevin"
"3 + 5"
"01234"
s = "first_index ... last_index"
s_l = len(s)
print(s_l)
print(s[0])
print(s[s_l-1])
# "a"
# 00
# "alphabet"
# 07
# print(name[0])
# 
expression = input("Enter expression: ")
first_number = expression[0]
second_number = expression[len(expression)-1]
operator = expression[2]

print(f"{first_number} {operator} {second_number} = {int(first_number) + int(second_number)}")






# ✅ STRING METHODS
# Python also provides a large assortment of
# methods to help work with strings

# lower, upper, strip

# find, replace, in (keyword)

# len, [] accessor, splicing



# ----------------------------
# Lesson 4: Lists, Tuples, Sets, and Dictionaries
# ----------------------------

# Common built in data structures for python

# ✅ LISTS
# Creates a list of items
# Think of a list whenever the order of items matters, and you expect to add, remove, or change items

# Declaration

# Adding To Lists

# Accessing Lists


# ✅ TUPLES
# Think of a tuple when you have a collection of items that represents a single, unchangeable thing. Once you create it, it should never be modified

# Pair of fixed data

# Declaration

# Accessing


# ✅ SETS
# Unordered, does not allow duplicate items
# Think of a set when all you care about is uniqueness and checking for an item's presence very quickly

# Unordered Structure of unique items

# Declaration

# Adding

# Accessing

# ✅ DICTIONARIES
# Think of a dictionary whenever you need to associate a specific piece of information (the value) with a unique identifier (the key)

# Structure with Key-Value pairs

# Declaration

# Adding

# ----------------------------
# Lesson 5: Mutable vs Immutable Types
# ----------------------------\

# ✅ WHAT IS MUTABILITY?

# Ability to change data in place.


# Immutable: int, float, str, tuple

# Mutable: list, dict, set

