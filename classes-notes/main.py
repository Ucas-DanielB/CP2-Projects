# Daniel Blanco, Classes and Object Notes

# What is a class in Python?
# -- A class is a blueprint for creating an object.
class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nHealth: {self.hp}\n Attack {self.dmg}"

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f"{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} now has {opponent.hp}")
            if opponent.hp > 0:
                self.hp -= opponent.dmg
                print(f"{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} now has {opponent.hp}")
                if self.hp <= 0:
                    print(f"{opponent.name} has been TKO'd {self.name} won the battle!")
            else:
                print(f"{opponent.name} has been TKO'd {self.name} won the battle!")


bob = pokemon("Mr.Bob", "Charizard", 300, 95)
fluffy = pokemon("Fluffy", "Arcanine", 280, 110)

print(bob.name)
print(fluffy.species)

bob.battle(fluffy)

# What is an object in python?
# -- An object is a specific instance of a class.

# How do python classes relate to python objects?
# -- A class is the blueprint and the object is the house built from the blueprint.

# How do you create a python class?
# -- You create a class by using the word "class", then the class name with a colon.

# What are methods?
# -- A method is a function specific to the class.

# How do you create a python object?
# -- You can create an object by calling the class, just like a function.

# How to you call a method for an object?
# -- You can call a method for an object by using a dot notation.

# Why do we use python classes?
# -- Python classes can help us organize our code better and reuse code.
