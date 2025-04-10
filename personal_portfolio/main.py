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
        "1. Personal Library (personal_P_library_MG.py)": "The project allows you to add, display, search, or remove books. The process of programming it was kind of annoying, as I couldn't get it right the first few times. I learned about different list types and how to utilize them in a project. This was an individual project.",
        "2. RPG Battle System (personal_battle_S.py)": "This project allowed the user to create characters and fight with them. It took me forever to finish the program, and proved to be one of the hardest programs to code I had done. I learned how to use dictionaries. This was an individual project.",
        "3. Finance Calculator (personal_finance_calc.py)": "A calculator made to budget allocate, time to save, compound/interest, sale price, and tip. The program was relatively easy to make, just figuring out how the math worked. I learned the different math calculations on code. This was an individual project.",
        "4. Movie Recommender (personal_movie_recommender.py)": "This project viewed movie recommendations and could filter to find something specific. This was a hard program to code, as getting the code right was tedious. I learned to use different files with information on them. This was an individual project.",
        "5. Tic Tac Toe (personal_tic_tac_toe.py)": "A Tic Tac Toe game. This i was one of the first hard projects to code, as I didn't quite understand the specifics to get right. I learned how to make my first visual, even if it used keyboard keys: |, x, o. This was an individual project.",
        "6. To-Do List (personal_to_do_list.py)": "A program that kept a list even after closing the terminal on a different file. It was new material, so it took me awhile to get the hang of txt files. I learned how to actually use txt files. This was an individual project."
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
