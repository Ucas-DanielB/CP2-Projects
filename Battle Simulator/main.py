# Daniel Blanco, Battle Simulator
import csv
import os
import random

CHARACTER_FILE = "characters.csv"

def main():
    "Main menu for RPG Character Management and Battle System."# The first thing user sees, you are able to create, view characters, start a battle and exit by inputting numbers
    while True:
        print("\nBattle Simulator")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Start Battle")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_character()
        elif choice == "2":
            display_characters()
        elif choice == "3":
            battle_system()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def create_character():
    "Creates a new character and saves it to a CSV file." # Create characters option from main menu is saved onto a csv file
    def get_valid_input(prompt, min_value=1, max_value=100):
        "Helper function to get valid integer input within a range."
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Please enter a value between {min_value} and {max_value}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    print("\nCreate a New Character") # Creating a character allows you to give them a name, their hp amount, strength, defense, and speed
    name = input("Enter character name: ").strip()
    health = get_valid_input("Enter Health (50-200): ", 50, 200)
    strength = get_valid_input("Enter Strength (5-50): ", 5, 50)
    defense = get_valid_input("Enter Defense (5-50): ", 5, 50)
    speed = get_valid_input("Enter Speed (1-20): ", 1, 20)
    # Creating a character always sets them to a level of 1 and experience to 0, these can be changed through winning battles
    level = 1
    experience = 0

    character = [name, health, strength, defense, speed, level, experience]
    save_character(character)
    print(f"Character '{name}' created successfully!")

def save_character(character): # This function has the created characters and saves them towards the csv file
    "Saves a character to the CSV file."
    file_exists = os.path.isfile(CHARACTER_FILE)
    with open(CHARACTER_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"])
        writer.writerow(character)

def load_characters(): # This function takes saved characters from the csv file and allows you to to view them in another function
    "Loads characters from the CSV file."
    if not os.path.isfile(CHARACTER_FILE):
        print("No characters found. Create a character first.")
        return []
    
    with open(CHARACTER_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row
        return [row for row in reader]

def display_characters(): # This displays all of the saved characters that were loaded
    "Displays all saved characters."
    characters = load_characters()
    if not characters:
        return

    print("\nSaved Characters:")
    for char in characters:
        print(f"Name: {char[0]}, Health: {char[1]}, Strength: {char[2]}, Defense: {char[3]}, Speed: {char[4]}, Level: {char[5]}, XP: {char[6]}")

def battle_system():
    "Manages turn-based battles between two characters with player choices."
    characters = load_characters()
    if len(characters) < 2:
        print("Not enough characters to start a battle. Create at least two.")
        return

    print("\nSelect two characters for battle:")
    for i, char in enumerate(characters):
        print(f"{i+1}. {char[0]}")
    
    try:
        p1_index = int(input("Select first character (number): ")) - 1
        p2_index = int(input("Select second character (number): ")) - 1
        if p1_index == p2_index or not (0 <= p1_index < len(characters)) or not (0 <= p2_index < len(characters)):
            print("Invalid selection. Please choose two different characters.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    player1 = convert_to_dict(characters[p1_index])
    player2 = convert_to_dict(characters[p2_index])

    print(f"\n{player1['Name']} VS {player2['Name']} - Battle Start!")

    while player1["Health"] > 0 and player2["Health"] > 0:
        turn(player1, player2)
        if player2["Health"] <= 0:
            print(f"{player1['Name']} wins!")
            player1["Experience"] += 10
            level_up(player1)
            break
        turn(player2, player1)
        if player1["Health"] <= 0:
            print(f"{player2['Name']} wins!")
            player2["Experience"] += 10
            level_up(player2)
            break

    update_character_stats(player1)
    update_character_stats(player2)

def turn(attacker, defender):
    "Handles a single turn where the player chooses an action."
    print(f"\n{attacker['Name']}'s turn!")
    print("1. Attack")
    print("2. Defend")
    print("3. Pass")
    choice = input("Choose an action: ").strip()

    if choice == "1":
        attack(attacker, defender)
    elif choice == "2":
        defender["Defense"] += 5
        print(f"{attacker['Name']} raises their defense!")
    elif choice == "3":
        print(f"{attacker['Name']} skips their turn.")
    else:
        print("Invalid choice, skipping turn.")

def attack(attacker, defender):
    "Calculates and applies attack damage."
    damage = max(1, attacker["Strength"] - defender["Defense"])
    defender["Health"] = max(0, defender["Health"] - damage)
    print(f"{attacker['Name']} attacks {defender['Name']} for {damage} damage! {defender['Name']} now has {defender['Health']} HP.")

def level_up(character):
    "Levels up a character if they gain enough experience."
    if character["Experience"] >= character["Level"] * 10:
        character["Level"] += 1
        character["Health"] += 10
        character["Strength"] += 2
        character["Defense"] += 2
        print(f"{character['Name']} has leveled up to Level {character['Level']}!")

def update_character_stats(character):
    "Updates a character’s stats in the CSV file after a battle."
    characters = load_characters()
    for i, char in enumerate(characters):
        if char[0] == character["Name"]:
            characters[i] = [character[key] for key in ["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"]]
    
    with open(CHARACTER_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"])
        writer.writerows(characters)

def convert_to_dict(character):
    "Converts a character list to a dictionary."
    keys = ["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"]
    return {keys[i]: int(character[i]) if i > 0 else character[i] for i in range(len(keys))}

if __name__ == "__main__":
    main()
