# Daniel Blanco, Battle Simulator

import csv
import os
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from faker import Faker

CHARACTER_FILE = "characters.csv"
fake = Faker()

def main():
    # Main menu Battle Simulator, allows you to create and view characters in different ways, then taking them to battle.
    while True:
        print("\nBattle Simulator")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Start Battle")
        print("4. Character Statistics")
        print("5. Visualize Character Stats")
        print("6. Exit")

        # Gets user choice
        choice = input("Enter your choice: ").strip()

        # Processes user choice
        if choice == "1":
            create_character()
        elif choice == "2":
            display_characters()
        elif choice == "3":
            battle_system()
        elif choice == "4":
            analyze_character_stats()
        elif choice == "5":
            visualize_character_stats()
        elif choice == "6":
            print("Goodbye!")
            break
        else: # Error Mesage
            print("Invalid choice. Please enter a number between 1 and 6.")

def create_character():
    # Creates a new character and saves it to a CSV file.
    def get_valid_input(prompt, min_value=1, max_value=100):
        # Helper function to get valid integer input within a range.
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else: # Error message
                    print(f"Please enter a value between {min_value} and {max_value}.")
            except ValueError: # Error message
                print("Invalid input. Please enter a number.")

    print("\nCreate a New Character")
    use_random = input("Generate a random character? (yes/no): ").strip().lower()
    # The process of making a character, this allwos you to generate a random character with info
    if use_random == "yes":
        name = fake.name()
        description = fake.sentence()
        health = random.randint(50, 200)
        strength = random.randint(5, 50)
        defense = random.randint(5, 50)
        speed = random.randint(1, 20)
    else: # The other option allows you to create your character with a name, description, health points, strength, defense, and speed
        name = input("Enter character name: ").strip()
        description = input("Enter character description: ").strip()
        health = get_valid_input("Enter Health (50-200): ", 50, 200)
        strength = get_valid_input("Enter Strength (5-50): ", 5, 50)
        defense = get_valid_input("Enter Defense (5-50): ", 5, 50)
        speed = get_valid_input("Enter Speed (1-20): ", 1, 20)
    # Level and experience cannot be changed by user input
    level = 1   # All characters start with level 1 and 0 experience
    experience = 0

    # Saves character info
    character = [name, description, health, strength, defense, speed, level, experience]
    save_character(character)
    print(f"Character '{name}' created successfully!")

def save_character(character):
    # Saves a character to the CSV file.
    file_exists = os.path.isfile(CHARACTER_FILE) # Appends on the existing character file
    with open(CHARACTER_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists: 
            writer.writerow(["Name", "Description", "Health", "Strength", "Defense", "Speed", "Level", "Experience"])
        writer.writerow(character)

def load_characters():
    # Loads characters from the CSV file into a Pandas DataFrame.
    if not os.path.isfile(CHARACTER_FILE):
        print("No characters found. Create a character first.")
        return pd.DataFrame()
    
    return pd.read_csv(CHARACTER_FILE)

def display_characters():
    # Displays all saved characters.
    df = load_characters()
    if df.empty:
        return

    print("\nSaved Characters:")
    print(df[["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"]].to_string(index=False))

def battle_system():
    # Manages turn-based battles between two characters.
    characters = load_characters()
    if len(characters) < 2:
        print("Not enough characters to start a battle. Create at least two.")
        return

    # Allow player to select two characters
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

    # Convert selected characters to dictionaries for easier manipulation
    player1 = {key: int(value) if key not in ["Name"] else value for key, value in zip(["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"], characters[p1_index])}
    player2 = {key: int(value) if key not in ["Name"] else value for key, value in zip(["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"], characters[p2_index])}

    # Determine attack order based on speed
    attacker, defender = (player1, player2) if player1["Speed"] > player2["Speed"] else (player2, player1)

    print(f"\n{player1['Name']} VS {player2['Name']} - Battle Start!")

    def battle_round(attacker, defender):
        # Handles a single attack round.
        damage = max(1, attacker["Strength"] - defender["Defense"])
        defender["Health"] = max(0, defender["Health"] - damage)
        print(f"{attacker['Name']} attacks {defender['Name']} for {damage} damage! {defender['Name']} now has {defender['Health']} HP.")

    while player1["Health"] > 0 and player2["Health"] > 0:
        battle_round(attacker, defender)
        if defender["Health"] == 0:
            print(f"{attacker['Name']} wins the battle!")
            attacker["Experience"] += 10
            level_up(attacker)
            break
        attacker, defender = defender, attacker  # Swap turns

    # Update characters in the CSV file after battle
    update_character_stats(player1)
    update_character_stats(player2)

def level_up(character):
    # Levels up a character if they gain enough experience.
    if character["Experience"] >= character["Level"] * 10:
        character["Level"] += 1
        character["Health"] += 10
        character["Strength"] += 2
        character["Defense"] += 2
        print(f"{character['Name']} has leveled up to Level {character['Level']}!")

def update_character_stats(character):
    # Updates a character’s stats in the CSV file after a battle.
    characters = load_characters()

    # Locate character in list and update stats
    for i, char in enumerate(characters):
        if char[0] == character["Name"]:
            characters[i] = [character[key] for key in ["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"]]

    # Write updated data back to CSV file
    with open(CHARACTER_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"])
        writer.writerows(characters)

def analyze_character_stats():
    # Performs statistical analysis on character attributes.
    df = load_characters()
    if df.empty:
        return

    print("\nCharacter Statistics:")
    stats = df[["Health", "Strength", "Defense", "Speed"]].describe()
    print(stats)

def visualize_character_stats():
    # Visualizes character stats using a bar graph or radar chart.
    df = load_characters()
    if df.empty:
        return
    
    print("\nSelect a character to visualize:")
    for i, name in enumerate(df["Name"], start=1):
        print(f"{i}. {name}")

    try: # Can select character by inputting numbers
        choice = int(input("Enter the character number: ")) - 1
        if choice < 0 or choice >= len(df):
            print("Invalid choice.") # Error message
            return
    except ValueError: # Error message
        print("Invalid input.")
        return

    # Chart that displays health, strength, defense, and speed
    char = df.iloc[choice]
    stats = ["Health", "Strength", "Defense", "Speed"]
    values = char[stats].values.astype(int)

    print("\nChoose visualization type:")
    print("1. Bar Graph")
    print("2. Radar Chart")
    vis_choice = input("Enter choice: ").strip()

    if vis_choice == "1": # User sees the choice to see characters stats and name
        plot_bar_chart(char["Name"], stats, values)
    elif vis_choice == "2":
        plot_radar_chart(char["Name"], stats, values)
    else:
        print("Invalid choice.") # Error message

def plot_bar_chart(name, labels, values):
    # Plots a bar chart for character stats.
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=["red", "blue", "green", "purple"])
    plt.xlabel("Attributes")
    plt.ylabel("Value")
    plt.title(f"{name}'s Stats")
    plt.show()

def plot_radar_chart(name, labels, values):
    # Plots a radar chart for character stats.
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values = np.concatenate((values, [values[0]]))
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color="blue", alpha=0.25)
    ax.plot(angles, values, color="blue", linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_title(f"{name}'s Stats")
    plt.show()

if __name__ == "__main__":
    main()
