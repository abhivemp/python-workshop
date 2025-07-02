```
"""
--- The Simple Zoo Manager (Advanced Edition) ---

Take your simple dictionary-based zoo program to the next level. 
Instead of storing dictionaries, you will now model each animal using a base 
`Animal` class and specialized subclasses for different types (e.g., Mammal, Bird), 
learning the powerful concept of inheritance.

--- Core Requirements ---

1.  Base `Animal` Class:
    - First, create a base class named `Animal`. It should manage the
      animal's `name`, `species`, and `habitat`.

2.  Specialized Subclasses:
    - Now, create at least two new classes that **inherit** from `Animal`:
      - `Mammal`: This class should have an additional attribute for `fur_color`.
      - `Bird`: This class should have an additional attribute for `wing_span`.

3.  User-Friendly Display (Method Overriding):
    - Implement a `__str__` method in each class (the base `Animal`, `Mammal`,
      and `Bird`) to create a custom, readable display. When printed, each
      object should show all of its relevant details. For example:
      - A `Mammal` might print: "Leo the Lion, lives in the Savannah, Fur: Golden"
      - A `Bird` might print: "Zazu the Hornbill, flies through the Savannah, Wingspan: 3ft"

4.  **Program Functionality:**
    - Your main "Add Animal" function will need a major update. It should now
      first ask the user what *type* of animal they are adding (e.g., Mammal
      or Bird).
    - Based on the user's choice, it should then ask for the information
      required for that specific subclass.
    - The program must create an instance of the correct class (`Mammal` or
      `Bird`) and add it to the zoo dictionary.
    - Your "View Animal" and "List All Animals" functions should be updated to
      work with your new animal objects.

--- Challenge: Unique Actions & Status ---

1.  Add a new attribute to the base `Animal` class to track a `status` (e.g.,
    "Hungry").
2.  Add a unique method to each subclass that represents a special action.
    - For `Mammal`, add a `groom()` method that prints a message like "Leo is grooming its golden fur."
    - For `Bird`, add a `fly()` method that prints "Zazu is soaring through the air!"
3.  Create new menu options to "Feed Animal" (which updates the status) and
    "Perform Special Action" (which calls the unique method). You will need
    to check an animal's type to see which action is available.

Example Session (with challenge):
--- Zoo Manager: Advanced ---
1. Add Animal
2. List All Animals
3. Feed Animal
4. Perform Special Action
5. Exit

Choose an option: 1
What type of animal? (Mammal/Bird): Mammal
Enter name: Leo
Enter species: Lion
Enter habitat: Savannah
Enter fur color: Golden
'Leo' the Lion has been added!

Choose an option: 2
--- All Animals in the Zoo ---
- Leo the Lion, lives in the Savannah (Hungry), Fur: Golden

Choose an option: 4
Which animal should perform an action? Leo
Leo is grooming its golden fur.
"""
```
