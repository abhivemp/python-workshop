'''
The Zoo Manager - Final Boss Edition

We are going to take the inheritance based zoo manager that you all worked on and add
the ability to load initial data from a CSV file and save any changes back to the file,
creating a persistent zoo environment.

There are two new requirements:
1. CSV Data Loading:
    Write a function that reads and parses data from a CSV file named my_zoo_data.csv.
    This function must be robust enough to:
        Read each row of the CSV.
        Identify the animal type ('Mammal' or 'Bird').
        Create an instance of the correct subclass based on the type.
        Use the data from the extra column to populate the unique attribute 
        of the subclass (fur_color for Mammals, wing_span for Birds).
    Your program should call this function automatically when it starts to 
    load the initial zoo population.

2. Save Zoo to CSV:
    Write a function that saves the current state of the zoo back to 
    my_zoo_data.csv, overwriting the existing file.
        This function will need to iterate through the animal objects 
        in your dictionary, check their type
        (e.g., using isinstance()), and write the correct data for each 
        column, including type and extra.
    Add this as an additional option

--- Challenge ---

Modify your save and load functions to handle the animal's hunger status. This will require adding
a status column to your CSV file and ensuring the state persists when the program restarts.

--- Initial Data from the Zoo in DC (create the my_zoo_data.csv using this 
data - be sure to remove any extra white space) ---

type,name,species,habitat,extra
Mammal,Bao Li,Giant Panda,Asia Trail,Black and white
Mammal,Qing Bao,Giant Panda,Asia Trail,Black and white
Mammal,Shaka,African Lion,Great Cats,Tawny
Mammal,Damai,Sumatran Tiger,Great Cats,Orange and black
Mammal,Baraka,Western Lowland Gorilla,Primates,Silverback
Mammal,Asa,Red Panda,Asia Trail,Reddish-brown
Mammal,Niko,Sloth Bear,Asia Trail,Shaggy black
Mammal,Spike,Asian Elephant,Elephant Trails,Gray
Mammal,Rainstorm,Alpaca,Kids' Farm,White
Mammal,Mateo,Maned Wolf,Claws & Paws Pathway,Reddish-brown
Bird,Rosie,American Flamingo,Bird House,5 ft
Bird,Justice,Bald Eagle,American Trail,8 ft
Bird,Sandy,Sandhill Crane,Bird House,6 ft
Bird,Rose,Roseate Spoonbill,Bird House,2.5 ft
Bird,Albert,Blue-billed Curassow,Bird House,3 ft
'''



import csv

class Animal:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat
        self.is_hungry = True

    def __str__(self):
        status = "Hungry" if self.is_hungry else "Fed"
        return f"{self.name} the {self.species}, lives in the {self.habitat} ({status})"

    def feed(self):
        """Marks the animal as fed."""
        self.is_hungry = False
        print(f"{self.name} has been fed!")

class Mammal(Animal):
    def __init__(self, name, species, habitat, fur_color):
        super().__init__(name, species, habitat)
        self.fur_color = fur_color

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Fur: {self.fur_color}"

    def groom(self):
        print(f"{self.name} is grooming its {self.fur_color} fur.")

class Bird(Animal):
    def __init__(self, name, species, habitat, wing_span):
        super().__init__(name, species, habitat)
        self.wing_span = wing_span

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Wingspan: {self.wing_span}"

    def fly(self):
        print(f"{self.name} is soaring through the air!")

def load_animals_from_csv(filename, database):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row.get('name')
                animal_type = row.get('type', '').lower()

                if not name or name in database:
                    continue

                if animal_type == 'mammal':
                    new_animal = Mammal(name, row['species'], row['habitat'], row['extra'])
                elif animal_type == 'bird':
                    new_animal = Bird(name, row['species'], row['habitat'], row['extra'])

                # Challenge: Load hunger status, defaulting to Hungry if column is missing
                status_str = row.get('status', 'Hungry').strip().lower()
                new_animal.is_hungry = (status_str == 'hungry')

                database[name] = new_animal
            print(f"Successfully loaded data from {filename}.")
    except FileNotFoundError:
        print(f"Warning: CSV file '{filename}' not found. Starting with an empty zoo.")
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")

def add_animal_to_zoo(database):
    animal_type = input("What type of animal? (Mammal/Bird): ").lower().strip()
    name = input("Enter name: ").strip()

    if name in database:
        print(f"An animal named '{name}' already exists in the zoo.")
        return

    species = input("Enter species: ").strip()
    habitat = input("Enter habitat: ").strip()

    if animal_type == "mammal":
        fur_color = input("Enter fur color: ").strip()
        new_animal = Mammal(name, species, habitat, fur_color)
    elif animal_type == "bird":
        wing_span = input("Enter wing span: ").strip()
        new_animal = Bird(name, species, habitat, wing_span)
    else:
        print("Invalid animal type. Please choose Mammal or Bird.")
        return

    database[name] = new_animal
    print(f"'{name}' the {species} has been added!")

def view_animal(database):
    name = input("Enter animal's name to view: ").strip()
    animal = database.get(name)
    if animal:
        print("\n--- Animal Profile ---")
        print(animal)
    else:
        print(f"'{name}' not found in the zoo.")

def list_all_animals(database):
    print("\n--- All Animals in the Zoo ---")
    if not database:
        print("The zoo is currently empty.")
        return
    for animal in database.values():
        print(f"- {animal}")

def feed_animal(database):
    name = input("Which animal would you like to feed? ").strip()
    animal = database.get(name)
    if animal:
        animal.feed()
    else:
        print(f"'{name}' not found in the zoo.")

def perform_special_action(database):
    name = input("Which animal should perform an action? ").strip()
    animal = database.get(name)

    if not animal:
        print(f"'{name}' not found in the zoo.")
        return

    if isinstance(animal, Mammal):
        animal.groom()
    elif isinstance(animal, Bird):
        animal.fly()
    else:
        print(f"{name} doesn't have a special action.")

def save_zoo_to_csv(filename, database):
    try:
        with open(filename, 'w') as file:
            #Add status challenge
            header = ['type', 'name', 'species', 'habitat', 'extra', 'status']
            writer = csv.writer(file)
            writer.writerow(header)

            for animal in database.values():
                animal_type = ""
                extra_info = ""
                if isinstance(animal, Mammal):
                    animal_type = "Mammal"
                    extra_info = animal.fur_color
                elif isinstance(animal, Bird):
                    animal_type = "Bird"
                    extra_info = animal.wing_span

                #For Hunger Challenge
                status = "Hungry" if animal.is_hungry else "Fed"

                writer.writerow([
                    animal_type,
                    animal.name,
                    animal.species,
                    animal.habitat,
                    extra_info,
                    status
                ])
        print(f"Zoo successfully saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving to the CSV file: {e}")


zoo_data_file = 'zoo_data_oop.csv'
zoo = {}
load_animals_from_csv(zoo_data_file, zoo)

while True:
    print("\n--- Zoo Manager: Inheritance ---")
    print("1. Add Animal")
    print("2. View Animal")
    print("3. List All Animals")
    print("4. Feed Animal")
    print("5. Perform Special Action")
    print("6. Save Zoo to File")
    print("7. Exit")
    choice = input("Choose an option: ").strip()

    if choice == '1':
        add_animal_to_zoo(zoo)
    elif choice == '2':
        view_animal(zoo)
    elif choice == '3':
        list_all_animals(zoo)
    elif choice == '4':
        feed_animal(zoo)
    elif choice == '5':
        perform_special_action(zoo)
    elif choice == '6':
        save_zoo_to_csv(zoo_data_file, zoo)
    elif choice == '7':
        print("Goodbye!")

        break
    else:
        print("Invalid option, please try again.")