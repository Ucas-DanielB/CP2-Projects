# Daniel blanco, Personal Portfolio

from personal_battle_S import *
from personal_finance_calc import *
from personal_movie_recommender import *
from personal_P_library_MG import *
from personal_morse_code import *
from personal_to_do_list import *

# Introduction
print("\nWelcome to Daniel Blanco's Personal Portfolio!")
print("This portfolio showcases several programming projects I've created.")
print("Use the menu to learn more about each project and run them if you'd like.\n")

def main(): 
    while True:
        print("\nPersonal Portfolio")
        print("1. To do List")
        print("2. Battle Simulator")
        print("3. Finance Calculator")
        print("4. Movie Recommender")
        print("5. Morse Code Translator")
        print("6. Personal Library")
        print("7. Exit Program")


        choice = int(input("What would you like to do (1-7)? "))
       
       # To Do List Code 
        if choice == 1: 
            print("This project takes parameters for diffrent movies then gives the users recomendations for movies they should watch")
            print("I found the coding process for this to be a little weird because I was initally overwhelmed by the amount of data on the list I had to sort through")
            print("Through this I learned basic file handling that i still use \n")
            main_1()
        

        # Battle Simulator Code
        elif choice == 2:
            print("This project takes an input from user for a phrase in english or more then translates between the two ")
            print("The coding process for this was fun because it was kinda like solving a puzzle in a way")
            print("I learned diffrent methods of handling user inputs\n")
            main_2() 
        
        # Finance Calculator Code
        elif choice == 3:
            print("This project is a password generator that generates passwords based on set parameters")
            print("I learned how to handle and save varibles to be reusewd in a seperate piece of code")
            print("I found the coding process to be relativly easy with the main issue being the creation of lists\n")
            main_3()
        
        # Movie Recommender Code 
        elif choice == 4:
            print("This project allows the user to create a to do list based on what they input")
            print("The coding process for this was fun because it allowed me to edit a file more then is usually done ")
            print("I learned about file editing and how to change an exiting file and modify prexisting elements\n ")
            main_4()
        
        # Morse Translator Program 
        elif choice == 5:
            print("This project takes the filepath for a txt document then gives the amount of words along with a time stamp on when it was last checked")
            print("I found the coding process for this to be quite unique becasue it required taking information from a none preset file")
            print("Through this I learned file handling for txts and how to use multiple python files\n")
            main_5()
        
        # Personal Library Code 
        elif choice == 6:
            print("This project takes inputs from user for what they want to use then runs the required ")
            print("I found the coding process for this to be a bit difficult because it was when I returned from coding after taking a year break")
            print("Through this I relearned several of the code basics I had forgotten\n")
            main_6()

        elif choice ==7:
            break

        else:
            print("Please select a number from 1-7")


    #descriptions = {
    ## This section of code goes over the details of each project
    ## Each discription goes overWhat the project does: How you found the programming process, What you learned, Your role (if it was a group project).
#
    #    "1. Personal Library (personal_P_library_MG.py)": "The project allows you to add, display, search, or remove books. The process of programming it was kind of annoying, as I couldn't get it right the first few times. I learned about different list types and how to utilize them in a project. This was an individual project.",
    #    "2. RPG Battle System (personal_battle_S.py)": "This project allowed the user to create characters and fight with them. It took me forever to finish the program, and proved to be one of the hardest programs to code I had done. I learned how to use dictionaries. This was an individual project.",
    #    "3. Finance Calculator (personal_finance_calc.py)": "A calculator made to allocate budget, time to save, compound/interest, sale price, and tip. The program was relatively easy to make, just figuring out how the math worked. I learned the different math calculations on code. This was an individual project.",
    #    "4. Movie Recommender (personal_movie_recommender.py)": "This project viewed movie recommendations and could filter to find something specific. This was a hard program to code, as getting the code right was tedious. I learned to use different files with information on them. This was an individual project.",
    #    "5. Tic Tac Toe (personal_tic_tac_toe.py)": "A Tic Tac Toe game. This was one of the first hard projects to code, as I didn't quite understand the specifics to get right. I learned how to make my first visual, even if it used keyboard keys: |, x, o. This was an individual project.",
    #    "6. To-Do List (personal_to_do_list.py)": "A program that kept a list even after closing the terminal on a different file. It was new material, so it took me a while to get the hang of txt files. I learned how to actually use txt files. This was an individual project."
    #}


    # This is the menu of the project descriptions
    # this print the descriptions, with the project you chose

    # User has to input a yes or no option, to see if they would like to run the code
    

if __name__ == "__main__":
    main()
