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
    """Main menu for RPG Character Management and Battle System."""
    while True:
        print("\nBattle Simulator")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Start Battle")
        print("4. Character Statistics")
        print("5. Visualize Character Stats")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

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
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def create_character():
    """Creates a new character and saves it to a CSV file."""
    def get_valid_input(prompt, min_value=1, max_value=100):
        """Helper function to get valid integer input within a range."""
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
    use_random = input("Generate a random character? (yes/no): ").strip().lower()
    
    if use_random == "yes":
        name = fake.name()
        description = fake.sentence()
        health = random.randint(50, 200)
        strength = random.randint(5, 50)
        defense = random.randint(5, 50)
        speed = random.randint(1, 20)
    else:
        name = input("Enter character name: ").strip()
        description = input("Enter character description: ").strip()
        health = get_valid_input("Enter Health (50-200): ", 50, 200)
        strength = get_valid_input("Enter Strength (5-50): ", 5, 50)
        defense = get_valid_input("Enter Defense (5-50): ", 5, 50)
        speed = get_valid_input("Enter Speed (1-20): ", 1, 20)

    level = 1
    experience = 0

    character = [name, description, health, strength, defense, speed, level, experience]
    save_character(character)
    print(f"Character '{name}' created successfully!")

def save_character(character):
    """Saves a character to the CSV file."""
    file_exists = os.path.isfile(CHARACTER_FILE)
    with open(CHARACTER_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Description", "Health", "Strength", "Defense", "Speed", "Level", "Experience"])
        writer.writerow(character)

def load_characters():
    """Loads characters from the CSV file into a Pandas DataFrame."""
    if not os.path.isfile(CHARACTER_FILE):
        print("No characters found. Create a character first.")
        return pd.DataFrame()
    
    return pd.read_csv(CHARACTER_FILE)

def display_characters():
    """Displays all saved characters."""
    df = load_characters()
    if df.empty:
        return

    print("\nSaved Characters:")
    print(df[["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"]].to_string(index=False))

def analyze_character_stats():
    """Performs statistical analysis on character attributes."""
    df = load_characters()
    if df.empty:
        return

    print("\nCharacter Statistics:")
    stats = df[["Health", "Strength", "Defense", "Speed"]].describe()
    print(stats)

def visualize_character_stats():
    """Visualizes character stats using a bar graph or radar chart."""
    df = load_characters()
    if df.empty:
        return
    
    print("\nSelect a character to visualize:")
    for i, name in enumerate(df["Name"], start=1):
        print(f"{i}. {name}")

    try:
        choice = int(input("Enter the character number: ")) - 1
        if choice < 0 or choice >= len(df):
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input.")
        return

    char = df.iloc[choice]
    stats = ["Health", "Strength", "Defense", "Speed"]
    values = char[stats].values.astype(int)

    print("\nChoose visualization type:")
    print("1. Bar Graph")
    print("2. Radar Chart")
    vis_choice = input("Enter choice: ").strip()

    if vis_choice == "1":
        plot_bar_chart(char["Name"], stats, values)
    elif vis_choice == "2":
        plot_radar_chart(char["Name"], stats, values)
    else:
        print("Invalid choice.")

def plot_bar_chart(name, labels, values):
    """Plots a bar chart for character stats."""
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=["red", "blue", "green", "purple"])
    plt.xlabel("Attributes")
    plt.ylabel("Value")
    plt.title(f"{name}'s Stats")
    plt.show()

def plot_radar_chart(name, labels, values):
    """Plots a radar chart for character stats."""
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
