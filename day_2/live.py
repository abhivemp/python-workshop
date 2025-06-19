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
# print(s_l)
# print(s[0])
# print(s[s_l-1])
# "a"
# 00
# "alphabet"
# 07
# print(name[0])
# 
# expression = input("Enter expression: ")
# first_number = expression[0]
# second_number = expression[len(expression)-1]
# operator = expression[2]

# print(f"{first_number} {operator} {second_number} = {int(first_number) + int(second_number)}")


# numbers = input("Input your numbers separated by a space")
# num1, num2 = numbers.split()
# num1 = float(num1.replace(","," "))
# num2 = float(num1.replace(","," "))
# result  = num1 + num2
# print(result)



# ✅ STRING METHODS
# Python also provides a large assortment of
# methods to help work with strings

# lower, upper, strip

# find, replace, in (keyword)

# s = "Pandas are cool"
# index = s.find("a", 2)
# # print(index)

# index = s.rfind("a")
# # print(index)

# s1 = "Rats are cool"
# print(s1)
# s1 = s1.replace("Rats", "Pandas")
# print(s1)

# len, [] accessor



# ----------------------------
# Lesson 4: Lists, Tuples, Sets, and Dictionaries
# ----------------------------

# Common built in data structures for python

# ✅ LISTS
# Creates a list of items
# Think of a list whenever the order of items matters, and you expect to add, remove, or change items

# # Declaration
# class_student_1 = "Neil"
# class_student_2 = "Nitya"

# # Fun fact, slicing aka substringing works with lists as well
# print(class_student_2[1:4])

# #           0        1          2         3         4
# session = ["Neil", "Nitya", "Gaurav", "Aashita", "Aiden"]
# #         -5         -4        -3         -2        -1
# # Adding To Lists
# # session.append("Soham")
# print(session)

# # Accessing Lists, using indexes
# print(session[0])
# print(session[len(session)-1])

# # fancy accessing
# # slicing using :
# # session[start:end:step]
# print(session[0:2]) # accesses the 0th and then the 1st
# print(session[2:])
# print(session[:2])



# ✅ TUPLES
# Think of a tuple when you have a collection of items that represents a single, unchangeable thing. Once you create it, it should never be modified


# Pair of fixed data
coordinates = (10.5, 20.5)

# Declaration

# Accessing
# print(coordinates)
# print(coordinates[1])

# ✅ SETS
# Unordered, does not allow duplicate items
# Think of a set when all you care about is uniqueness and checking for an item's presence very quickly

# Unordered Structure of unique items

# Declaration
# nums = {1,2,3,4,5}
# print(nums)
# nums = {1,2,3,4,5,4}
# print(nums)


# # Adding

# nums.add(5)
# print(nums)
# nums.add(8)
# print(nums)
# # Accessing
# print(19 in nums)

# ✅ DICTIONARIES
# Think of a dictionary whenever you need to associate a specific piece of information 
# (the value) with a unique identifier (the key)

# Structure with Key-Value pairs
exampleDictionary = {
    "apple" : "Fruit that grows on tree",
}
# Declaration
person = {
    "name" : "kevin",
    "age" : 24,
    "is_student" : False
}
# Adding
print(person)
person["career"] = "SWE"
print(person)
print(person.keys())

# ----------------------------
# Lesson 5: Mutable vs Immutable Types
# ----------------------------\

# ✅ WHAT IS MUTABILITY?

# Ability to change data in place.


# Immutable: int, float, str, tuple

# Mutable: list, dict, set

