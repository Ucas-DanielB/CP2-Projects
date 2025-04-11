# main.py

from InquirerPy import prompt
import subprocess

# Introduction
print("\nWelcome to Daniel Blanco's Personal Programming Portfolio!")
print("This portfolio showcases several programming projects I've created.")
print("Use the menu to learn more about each project and run them if you'd like.\n")

def main():
    questions = [
        {
            "type": "list",
            "message": "Select a project to learn more or run:",
            "name": "project",
            "choices": [
                "1. Personal Library (personal_P-library-MG.py)",
                "2. RPG Battle System (personal_battle_S.py)",
                "3. Finance Calculator (personal_finance-calc.py)",
                "4. Movie Recommender (personal_movie-recommender.py)",
                "5. Tic Tac Toe (personal_tic-tac-toe.py)",
                "6. To-Do List (personal_to-do-list V2.py)",
                "Exit"
            ]
        }
    ]

    answer = prompt(questions)
    project = answer["project"]

    if project == "Exit":
        print("Thanks for visiting my portfolio!")
        return

    descriptions = {
        "1. Personal Library (personal_P-library-MG.py)": "NOTE",
        "2. RPG Battle System (personal_battle_S.py)": "NOTE",
        "3. Finance Calculator (personal_finance-calc.py)": "NOTE",
        "4. Movie Recommender (personal_movie-recommender.py)": "NOTE",
        "5. Tic Tac Toe (personal_tic-tac-toe.py)": "NOTE",
        "6. To-Do List (personal_to-do-list V2.py)": "NOTE"
    }

    print("\n--- Project Description ---")
    print(f"{descriptions[project]}\n")

    run_question = [
        {
            "type": "confirm",
            "message": "Would you like to run this project?",
            "name": "run"
        }
    ]

    should_run = prompt(run_question)["run"]

    if should_run:
        filename = project.split('(')[1].split(')')[0]
        try:
            subprocess.run(["python", filename])
        except Exception as e:
            print(f"Failed to run {filename}: {e}")

    main()  # restart menu

if __name__ == "__main__":
    main()
