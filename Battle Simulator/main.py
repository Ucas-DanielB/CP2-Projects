# Daniel Blanco, Battle Simulator
import csv
import os
import random

CHARACTER_FILE = "characters.csv"

def main(): # The first thing the user sees, by inputting numbers they can create and view their characters, and also start battles
    "Main menu for RPG Character Management and Battle System."
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

def create_character(): # Creates a character, user can give them a name, amount of health, strength, defense, and speed
    "Creates a new character and saves it to a CSV file."
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

    print("\nCreate a New Character")
    name = input("Enter character name: ").strip()
    health = get_valid_input("Enter Health (50-200): ", 50, 200)
    strength = get_valid_input("Enter Strength (5-50): ", 5, 50)
    defense = get_valid_input("Enter Defense (5-50): ", 5, 50)
    speed = get_valid_input("Enter Speed (1-20): ", 1, 20)
    level = 1
    experience = 0
# Every character thats created starts automatically with one level and zero experience
    character = [name, health, strength, defense, speed, level, experience]
    save_character(character)
    print(f"Character '{name}' created successfully!")

def save_character(character): # newly created characters are saved onto a csv file
    """Saves a character to the CSV file without overwriting existing ones."""
    file_exists = os.path.isfile(CHARACTER_FILE)
    
    with open(CHARACTER_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"])
        writer.writerow(character)

def load_characters(): # If called, created characters can be viewed are brought to battle
    "Loads characters from the CSV file, ensuring correct data format."
    if not os.path.isfile(CHARACTER_FILE):
        return []
    
    characters = []
    with open(CHARACTER_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        headers = next(reader, None)  # Read headers and ignore them in data
        for row in reader:
            if len(row) == 7:
                characters.append(row)
    
    return characters

def display_characters(): # loaded characters can be displayed with their stats
    "Displays all saved characters."
    characters = load_characters()
    if not characters:
        print("No characters found. Create one first.")
        return

    print("\nSaved Characters:")
    for char in characters:
        print(f"Name: {char[0]}, Health: {char[1]}, Strength: {char[2]}, Defense: {char[3]}, Speed: {char[4]}, Level: {char[5]}, XP: {char[6]}")

def battle_system(): # starts the turn based battle
    "Manages turn-based battles where players choose actions."
    characters = load_characters()
    if len(characters) < 2:
        print("Not enough characters to start a battle. Create at least two.")
        return

    print("\nSelect two characters for battle:")
    for i, char in enumerate(characters):
        print(f"{i+1}. {char[0]}")
    # selecting characters to fight, must require at least two characters to fight
    try:
        p1_index = int(input("Select first character (number): ")) - 1
        p2_index = int(input("Select second character (number): ")) - 1
        if p1_index == p2_index or not (0 <= p1_index < len(characters)) or not (0 <= p2_index < len(characters)):
            print("Invalid selection. Please choose two different characters.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    player1 = characters[p1_index]
    player2 = characters[p2_index]
    # battle 
    player1 = {key: int(value) if key not in ["Name"] else value for key, value in zip(
        ["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"], player1)}
    player2 = {key: int(value) if key not in ["Name"] else value for key, value in zip(
        ["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"], player2)}

    print(f"\n{player1['Name']} VS {player2['Name']} - Battle Start!")

    while player1["Health"] > 0 and player2["Health"] > 0:
        for attacker, defender in [(player1, player2), (player2, player1)]:
            print(f"\n{attacker['Name']}'s turn! Choose an action:")
            print("1. Attack")
            print("2. Defend")
            
            action = input("Enter your choice: ").strip()
            if action == "1":
                damage = max(1, attacker["Strength"] - defender["Defense"] // 2)
                defender["Health"] = max(0, defender["Health"] - damage)
                print(f"{attacker['Name']} attacks {defender['Name']} for {damage} damage!")
            elif action == "2":
                attacker["Defense"] += 2
                print(f"{attacker['Name']} braces for impact, increasing defense!")

            if defender["Health"] == 0:
                print(f"{attacker['Name']} wins the battle!")
                attacker["Experience"] += 10
                level_up(attacker)
                update_character_stats(player1)
                update_character_stats(player2)
                return

def level_up(character): # After every battle, the winner gains a level and a boost in stats
    "Levels up a character if they gain enough experience."
    if character["Experience"] >= character["Level"] * 10:
        character["Level"] += 1
        character["Health"] += 10
        character["Strength"] += 2
        character["Defense"] += 2
        print(f"{character['Name']} has leveled up to Level {character['Level']}!")

def update_character_stats(character): Characters that win have their new levels, experience, and stats updated to the csv file
    "Updates an existing character’s stats in the CSV file after a battle."
    characters = load_characters()
    
    for i, char in enumerate(characters):
        if char[0] == character["Name"]:  # Match by name
            characters[i] = [
                character["Name"], character["Health"], character["Strength"], 
                character["Defense"], character["Speed"], character["Level"], character["Experience"]
            ]
    
    with open(CHARACTER_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"])
        writer.writerows(characters)

if __name__ == "__main__":
    main()
