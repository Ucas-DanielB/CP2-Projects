import random
import json

class Pet:
    def __init__(self, name, species, age=0):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.health = 100
        self.level = 1
        self.skills = []

    def feed(self, food):
        effects = {
            "kibble": (10, 5),
            "treat": (5, 15),
            "meat": (20, 10)
        }
        if food in effects:
            hunger_change, happiness_change = effects[food]
            self.hunger = max(0, self.hunger - hunger_change)
            self.happiness = min(100, self.happiness + happiness_change)
            self._advance_time()
        else:
            print("Unknown food type.")

    def play(self):
        if self.energy >= 10:
            self.happiness = min(100, self.happiness + 20)
            self.energy -= 10
            self.hunger = min(100, self.hunger + 10)
        else:
            print(f"{self.name} is too tired to play.")
        self._advance_time()

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.hunger = min(100, self.hunger + 5)
        self._advance_time()

    def status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Species: {self.species}, Age: {self.age}, Level: {self.level}")
        print(f"Hunger: {self.hunger}, Happiness: {self.happiness}")
        print(f"Energy: {self.energy}, Health: {self.health}")
        print(f"Skills: {', '.join(self.skills) if self.skills else 'None'}\n")

    def _advance_time(self):
        self.age += 0.1
        self._update_health()
        self._random_event()
        self._check_level_up()

    def _update_health(self):
        if self.hunger > 80 or self.energy < 20 or self.happiness < 30:
            self.health -= 5
        else:
            self.health = min(100, self.health + 1)

    def _random_event(self):
        event = random.choice([None, "sick", "found toy"])
        if event == "sick":
            print(f"{self.name} got sick! -10 health.")
            self.health = max(0, self.health - 10)
        elif event == "found toy":
            print(f"{self.name} found a toy! +10 happiness.")
            self.happiness = min(100, self.happiness + 10)

    def _check_level_up(self):
        if self.age >= self.level * 1.5:
            self.level += 1
            new_skill = f"Skill{self.level}"
            self.skills.append(new_skill)
            print(f"{self.name} leveled up! Learned {new_skill}.")

# Save/Load System
def save_pets(pet_list, filename='pets.json'):
    with open(filename, 'w') as f:
        json.dump([pet.__dict__ for pet in pet_list], f)

def load_pets(filename='pets.json'):
    try:
        with open(filename, 'r') as f:
            pet_data = json.load(f)
            return [Pet(**data) for data in pet_data]
    except FileNotFoundError:
        return []

# Text-based UI
def main_menu():
    pets = load_pets()
    current_pet = None

    while True:
        print("\n--- Pet Simulator ---")
        print("1. Create Pet")
        print("2. Switch Pet")
        print("3. Show Status")
        print("4. Feed Pet")
        print("5. Play with Pet")
        print("6. Put Pet to Sleep")
        print("7. Save and Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Pet's name: ")
            species = input("Pet's species: ")
            pet = Pet(name, species)
            pets.append(pet)
            current_pet = pet
        elif choice == "2":
            for i, pet in enumerate(pets):
                print(f"{i + 1}. {pet.name}")
            idx = int(input("Select pet number: ")) - 1
            if 0 <= idx < len(pets):
                current_pet = pets[idx]
        elif choice == "3":
            if current_pet:
                current_pet.status()
            else:
                print("No pet selected.")
        elif choice == "4":
            if current_pet:
                food = input("Food (kibble/treat/meat): ").lower()
                current_pet.feed(food)
            else:
                print("No pet selected.")
        elif choice == "5":
            if current_pet:
                current_pet.play()
            else:
                print("No pet selected.")
        elif choice == "6":
            if current_pet:
                current_pet.sleep()
            else:
                print("No pet selected.")
        elif choice == "7":
            save_pets(pets)
            print("Game saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
