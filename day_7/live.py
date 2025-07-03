# ----------------------------
# Lesson 17: Inheritance and Polymorphism
# ----------------------------


# Inheritance allows one class (child/subclass) to inherit the properties and methods of another (parent/superclass).
# This supports code reuse and hierarchical modeling.

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def display_info(self):
#         print(f"{self.year} {self.make} {self.model}")

# # () and putting the parent class declares the inheritance
# class Car(Vehicle):
#     def __init__(self, make, model, year, num_doors):
#         #call the parent's constructor aka __init__ function
#         super().__init__(make, model, year)
#         self.num_doors = num_doors

#     # def display_info(self):
#     #     print(f"{self.year} {self.make} {self.model}, {self.num_doors}-door ")

# my_first_car = Car("Porchse", "GT2 RS", "2018", "2")
# my_first_car.display_info()

# Polymorphism means "many forms".
# It allows objects of different classes to be treated through a shared interface (like calling the same method on different objects).

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")


animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()

Dog().speak()
# ----------------------------
# Lesson 18: Abstract Classes and Interfaces (abc module)
# ----------------------------

# An abstract class provides a template for other classes.
# Use the `abc` module and the `@abstractmethod` decorator to require that subclasses implement certain methods.
# Abstract base classes enforce consistency in APIs, especially when working with teams or frameworks.

# Abstract Base Class Structure

# ----------------------------
# Lesson 19: Magic Methods
# ----------------------------

# Magic Methods
# Magic methods start and end with double underscores.
# They allow classes to integrate with Python’s built-in functions and operations.

#__str__

#__repr__

#__len__

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"HERE PRESENTS THE BOOK: {self.title}"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    def __len__(self):
        return self.pages

my_book = Book("How to be a millionare", 600)
print(my_book)
print(repr(my_book))
print(len(my_book))
