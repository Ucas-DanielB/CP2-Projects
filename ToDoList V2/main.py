#Daniel Blanco, To Do List

#Create a program that allows the user to view, add, delete, and mark tasks on a to do list that is saved on a seperate text file. 

#REQUIREMENTS:
#Create a to do list (Kept on a txt file)
#Add items to the to do list
#Mark item as complete
#Delete item from to do list

#r = read (won’t create file)
#w = write (won’t create file)
#w+ = read and write
#a = append (add things but not write over) (Will create the file if it isn’t there)
#x = create a file

#example: 

#with open(‘Notes_2nd/things.txt’, “w”) as file:
	#File.write(“\nI just made another line on my file!”)

#with open(‘Notes_2nd/things.txt’, “r”) as file:
	#print(file.read())

#Read and write you do the same but just have both of them in the same space of code.

#File.write(“”) as file:
#print(file.read())

def add_items():
    with open("ToDoList V2/ToDoList.txt", "w") as file:
        file.write("\nLook ma Im doing it")