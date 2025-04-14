# Daniel Blanco, Classes and Object Notes

# A class is a blueprint for creating an object.
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

# A method is a function specific to the class.
# An object is a specific instance of a class.