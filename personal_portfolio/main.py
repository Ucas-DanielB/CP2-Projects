# Daniel blanco, Personal Portfolio

from InquirerPy import prompt
import subprocess
from personal_movie_recommender import *

# Introduction
print("\nWelcome to Daniel Blanco's Personal Programming Portfolio!")
print("This portfolio showcases several programming projects I've created.")
print("Use the menu to learn more about each project and run them if you'd like.\n")

def main():

# The main user interface, gives a list of 7 options, allowing the user to choose 6 different projects to see
    questions = [
        {
            "type": "list",
            "message": "Select a project to learn more or run:",
            "name": "project",
            "choices": [
                "1. Personal Library (personal_P_library_MG.py)",
                "2. RPG Battle System (personal_battle_S.py)",
                "3. Finance Calculator (personal_finance_calc.py)",
                "4. Movie Recommender (personal_movie_recommender.py)",
                "5. Tic Tac Toe (personal_tic_tac_toe.py)",
                "6. To-Do List (personal_to_do_list.py)",
                "Exit"
            ]
        }
    ]

    answer = prompt(questions)
    print(f"This is the 'answer' the user is giving {answer}")
    project = answer["project"]
    print(f"This is the project: {project}")

    # This closes the program and prints a goodbye message
    if project == "Exit":
        print("Thanks for visiting my portfolio!")
        return

    descriptions = {
    # This section of code goes over the details of each project
    # Each discription goes overWhat the project does: How you found the programming process, What you learned, Your role (if it was a group project).

        "1. Personal Library (personal_P_library_MG.py)": "The project allows you to add, display, search, or remove books. The process of programming it was kind of annoying, as I couldn't get it right the first few times. I learned about different list types and how to utilize them in a project. This was an individual project.",
        "2. RPG Battle System (personal_battle_S.py)": "This project allowed the user to create characters and fight with them. It took me forever to finish the program, and proved to be one of the hardest programs to code I had done. I learned how to use dictionaries. This was an individual project.",
        "3. Finance Calculator (personal_finance_calc.py)": "A calculator made to allocate budget, time to save, compound/interest, sale price, and tip. The program was relatively easy to make, just figuring out how the math worked. I learned the different math calculations on code. This was an individual project.",
        "4. Movie Recommender (personal_movie_recommender.py)": "This project viewed movie recommendations and could filter to find something specific. This was a hard program to code, as getting the code right was tedious. I learned to use different files with information on them. This was an individual project.",
        "5. Tic Tac Toe (personal_tic_tac_toe.py)": "A Tic Tac Toe game. This was one of the first hard projects to code, as I didn't quite understand the specifics to get right. I learned how to make my first visual, even if it used keyboard keys: |, x, o. This was an individual project.",
        "6. To-Do List (personal_to_do_list.py)": "A program that kept a list even after closing the terminal on a different file. It was new material, so it took me a while to get the hang of txt files. I learned how to actually use txt files. This was an individual project."
    }


    # This is the menu of the project descriptions
    print("\n--- Project Description ---")
    # this print the descriptions, with the project you chose
    print(f"{descriptions[project]}\n")

    # User has to input a yes or no option, to see if they would like to run the code
    run_question = [
        {
            "type": "confirm",
            "message": "Would you like to run this project?",
            "name": "run"
        }
    ]


    should_run = prompt(run_question)["run"]

    # it takes into account of the users request, y/n, and runs the program
    if should_run:
        filename = project.split('(')[1].split(')')[0]
        try:
            subprocess.run(["python", filename])
        # Error message, the program didn't start
        except Exception as e:
            print(f"Failed to run {filename}: {e}")

#    if should_run:
#        file_to_run = projects[project_name]
#        if os.path.isfile(file_to_run):
#            try:
#                subprocess.run([sys.executable, file_to_run])
#            except Exception as e:
#                print(f"An error occurred while running the file: {e}")
#        else:
#            print(f"Error: '{file_to_run}' not found. Please make sure the file is in the same folder.")

if __name__ == "__main__":
    main()
