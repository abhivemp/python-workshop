# Write a Python program that generates a random number 
# between 1 and 100, and asks the user to guess it.

# The game should tell the user whether their guess is 
# too high, too low, or correct, and keep looping until 
# they guess correctly. At the end, tell them how many tries it took.
# Include a function that checks the users guesses

# import random

# def check_guess(secret_number, guess):
#     if guess < secret_number:
#         return "Too low!"
#     elif guess > secret_number:
#         return "Too high!"
#     else:
#         return "Correct!"

# print("I'm thinking of a number between 1 and 100...")
# secret_number = random.randint(1, 100)
# attempts = 0
# guess = -1

# while guess != secret_number:
#     guess = int(input("Enter your guess: "))
#     attempts += 1
#     result = check_guess(secret_number, guess)
#     print(result)

# print(f"You got it in {attempts} tries")



"""
--- The Simple Zoo Manager ---

Objective:
Write a program to keep track of the animals in a small zoo.

Your program will manage a dictionary called `zoo`. The keys of this
dictionary will be the animal's name (e.g., "Po"), and the values will be
another dictionary containing that animal's details (e.g.,
{'species': 'Panda', 'habitat': 'Bamboo Forest'}).

You must create and use the following two functions:

1.  add_animal
    - Prompts the user for the new animal's `name`, its `species`
      (e.g., "Tiger", "Snake"), and its `habitat` (e.g., "Jungle", "Rain Forest").
    - Adds the new animal's profile to the dictionary.
    - Includes a check to prevent adding an animal if its name already exists.


2.  list_all_animals
    - Loops through all the animals in the database and prints a simple
      summary of each one (e.g., "Po the Panda").
    - If the zoo is empty, it should print a message saying so.

Finally, create a menu of options to the user
(Add Animal, List All Animals, Exit)

Example Session:
--- Simple Zoo Manager ---
1. Add Animal
2. List All Animals
3. Exit

Choose an option: 1
Enter the animal's name: Po
Enter the species: Panda
Enter the habitat: Bamboo Forest
'Po' has been added to the zoo!

Choose an option: 2
--- All Animals in the Zoo ---
- Po the Panda

Choose an option: 3
Goodbye!
"""




# ----------------------------
# Lesson 13: Classes and Objects
# ----------------------------

# A class is a blueprint for creating objects (also known as instances).
# Objects bundle together data (attributes) and behavior (methods).

# Class definition structure 
class Dog: 
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()

# `__init__` is a special method that gets called when a new object is created.
# It's used to initialize (set up) the object's attributes.

class Cat:
    def __init__(self, name):
        self.name = name
    
    def meow(self):
        print(f"{self.name} says Meow!")

my_cat = Cat("Whiskers")
my_second_cat = Cat("Garfield")
my_cat.meow()
my_second_cat.meow()


# `self` refers to the current object instance.
# It lets you access instance variables and methods from within the class.

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Yo!! wsg. The name is {self.name}")
# Think of `self` as the way each object keeps track of its own data.
kevin = Person("Kevin")
kevin.greet()

# What is "Person"? Is it a variable?
print(type(Person))
print(type(11))
print(type(kevin))
# ----------------------------
# Lesson 16: Attributes
# ----------------------------

# Instance Attributes
# These are variables that belong to a specific object.
# They are typically set in the `__init__` method using `self`.

class Car:
    def __init__(self, color, make, hp):
        self.color = color
        self.make = make
        self.hp = float(hp)

accord = Car("Black", "Honda", "200")
print(accord.make)
print(accord.hp)

# Class Attributes"
# These are shared across all instances of the class.
# They are defined directly within the class body and not inside `__init__`.

class Circle:
    pi = 3.141519
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.pi * self.radius ** 2

circle1 = Circle(5)
print("Area of the circle: ", circle1.area())

## Close off for the day:

# Bank Account Exercise

# Create a BankAccount class.
# The class must have the following attributes:
#   owner_name
#   balance (should start at 0)
# The class must have the following methods:
#   deposit(amount): Adds money to the balance.
#   withdraw(amount): Removes money from the balance, but only if there are enough funds.
#   check_balance(): Displays the owner's name and current balance.
# Create an interactive loop that allows a user to create an account and then choose to deposit, withdraw, check their balance, or exit the program.