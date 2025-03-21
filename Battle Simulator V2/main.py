# Daniel Blanco, Updated Battle Simulator

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
    #Main menu for the updated battle simulator, allows you to create, view, fight with, view stats, and visualize character stats 
    while True:
        print("\nBattle Simulator")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Start Battle")
        print("4. Character Statistics")
        print("5. Visualize Character Stats")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()


        # By inputting numbers, you are able to interact with the menu
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
        else: # Not inputting a number between the numbers 1 and 6 prints this error message
            print("Invalid choice. Please enter a number between 1 and 6.")



def create_character():
    # When inputting 1 from the menu, it allows you to create a character which is this function
    def get_valid_input(prompt, min_value=1, max_value=100):
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    # Error message appears when not inputting a number between the lowest and max range
                    print(f"Please enter a value between {min_value} and {max_value}.")
            except ValueError:
                # Error message appears when not inputting a number
                print("Invalid input. Please enter a number.")


    
    print("\nCreate a New Character")
    # When creating a character, you are also given the option for a random character to be generated for you
    use_random = input("Generate a random character? (yes/no): ").strip().lower()
    
    # If function to determine information for the character, such as name, description, health points, strength, defense, and speed
    if use_random == "yes":
        name = fake.name()
        description = fake.sentence()
        health = random.randint(50, 200)
        strength = random.randint(5, 50)
        defense = random.randint(5, 50)
        speed = random.randint(1, 20)
    else:
        # Choosing to create a characyer allows you to choose their name, description, health points, strength, defense, and speed
        name = input("Enter character name: ").strip()
        description = input("Enter character description: ").strip()
        health = get_valid_input("Enter Health (50-200): ", 50, 200)
        strength = get_valid_input("Enter Strength (5-50): ", 5, 50)
        defense = get_valid_input("Enter Defense (5-50): ", 5, 50)
        speed = get_valid_input("Enter Speed (1-20): ", 1, 20)

    # Every new character starts with 1 level and 0 experience, this cannot be purposely changed by the user
    level = 1
    experience = 0

    # All of the character information is saved onto a csv file

    character = [name, description, health, strength, defense, speed, level, experience]
    save_character(character)
    print(f"Character '{name}' created successfully!")


# This function does the process of saving a character towards a csv file

def save_character(character):
    file_exists = os.path.isfile(CHARACTER_FILE)
    with open(CHARACTER_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Description", "Health", "Strength", "Defense", "Speed", "Level", "Experience"])
        writer.writerow(character)


# This function Loads characters from the CSV file into a Pandas DataFrame

def load_characters():
    if not os.path.isfile(CHARACTER_FILE):
        print("No characters found. Create a character first.")
        return pd.DataFrame()
    
    return pd.read_csv(CHARACTER_FILE)


# Saved and loaded characters can be displayed, this option is available from the menu by inputting 2

def display_characters():
    df = load_characters()
    if df.empty:
        return
    # Prints the information for saved characters
    print("\nSaved Characters:")
    print(df[["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"]].to_string(index=False))


# When inputting 4 from the menu, the code runs a stats analysis on a characters attributes

def analyze_character_stats():
    df = load_characters()
    if df.empty:
        return
    # Prints all the character information 
    print("\nCharacter Statistics:")
    stats = df[["Health", "Strength", "Defense", "Speed"]].describe()
    print(stats)


# When inputting 5 from the menu, the code presents a visualization of the character stats by using a bar graph or radar chart

def visualize_character_stats():
    df = load_characters()
    if df.empty:
        return
    # Allows you  to select a specific character by number
    print("\nSelect a character to visualize:")
    for i, name in enumerate(df["Name"], start=1):
        print(f"{i}. {name}")

    try: # the process of selecting a character
        choice = int(input("Enter the character number: ")) - 1
        if choice < 0 or choice >= len(df):
            # Error message if the wrong number was inputted
            print("Invalid choice.")
            return
    except ValueError:
        # Error message if a number was not inputted
        print("Invalid input.")
        return


    char = df.iloc[choice]
    stats = ["Health", "Strength", "Defense", "Speed"]
    values = char[stats].values.astype(int)

    # Allows you to choose how you would like to see the stats

    print("\nChoose visualization type:")
    print("1. Bar Graph")
    print("2. Radar Chart")
    vis_choice = input("Enter choice: ").strip()
    # Choice must be made with numbers
    if vis_choice == "1":
        plot_bar_chart(char["Name"], stats, values)
    elif vis_choice == "2":
        plot_radar_chart(char["Name"], stats, values)
    else: # Error message if a number was not inputted
        print("Invalid choice.")


# This function plots a bar chart for character stats

def plot_bar_chart(name, labels, values):
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=["red", "blue", "green", "purple"])
    plt.xlabel("Attributes")
    plt.ylabel("Value")
    plt.title(f"{name}'s Stats")
    plt.show()


# This function plots a radar chart for character stats

def plot_radar_chart(name, labels, values):
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