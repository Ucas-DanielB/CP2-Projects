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
    # This section of code goes over the details of each project
    # Each discription goes overWhat the project does: How you found the programming process, What you learned, Your role (if it was a group project).
            print("A program that kept a list even after closing the terminal on a different file.")
            print("It was new material, so it took me a while to get the hang of txt files.")
            print("I learned how to actually use txt files. This was an individual project.\n")
            main_1()
        

        # Battle Simulator Code
        elif choice == 2:
    # This section of code goes over the details of each project
    # Each discription goes overWhat the project does: How you found the programming process, What you learned, Your role (if it was a group project).
            print("This project allowed the user to create characters and fight with them.")
            print("It took me forever to finish the program, and proved to be one of the hardest programs to code I had done.")
            print("I learned how to use dictionaries. This was an individual project.\n")
            main_2() 
        
        # Finance Calculator Code
        elif choice == 3:
    # This section of code goes over the details of each project
    # Each discription goes overWhat the project does: How you found the programming process, What you learned, Your role (if it was a group project
            print("A calculator made to allocate budget, time to save, compound/interest, sale price, and tip.")
            print("The program was relatively easy to make, just figuring out how the math worked.")
            print("I learned the different math calculations on code. This was an individual project.\n")
            main_3()
        
        # Movie Recommender Code 
        elif choice == 4:
    # This section of code goes over the details of each project
    # Each discription goes overWhat the project does: How you found the programming process, What you learned, Your role (if it was a group project).
            print("This project viewed movie recommendations and could filter to find something specific.")
            print("This was a hard program to code, as getting the code right was tedious.")
            print("I learned to use different files with information on them. This was an individual project.\n ")
            main_4()
        
        # Morse Translator Program 
        elif choice == 5:
    # This section of code goes over the details of each project
    # Each discription goes overWhat the project does: How you found the programming process, What you learned, Your role (if it was a group project).
            print("This")
            print("")
            print("\n")
            main_5()
        
        # Personal Library Code 
        elif choice == 6:
    # This section of code goes over the details of each project
    # Each discription goes overWhat the project does: How you found the programming process, What you learned, Your role (if it was a group project).
            print("The project allows you to add, display, search, or remove books.")
            print("The process of programming it was kind of annoying, as I couldn't get it right the first few times.")
            print("I learned about different list types and how to utilize them in a project. This was an individual project.\n")
            main_6()

        elif choice ==7:
            break

        else:
            print("Please select a number from 1-7")


if __name__ == "__main__":
    main()
