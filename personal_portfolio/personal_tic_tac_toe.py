#Create a game that allows a user to play tic-tac-toe. 

#The board needs to be made out of a list of lists (3 lists, one for each row)

#The program needs to use a nested for loop to print the board after each turn

#The program needs to use random to have a computer play for O (your user will be X)

#Make sure user instructions are clear on how to play and make sure you check for a winner after each turn (This should be a function with conditionals for the different win conditions).

import random

board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_board_full():
    for row in board:
        if " " in row:
            return False
    return True

print("Welcome to Tic-Tac-Toe!")
print("You are X, and the computer is O.")
print("To make a move, enter the row and column numbers (0, 1, or 2).")
print_board()

while True:
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")
    print_board()

    winner = check_winner()
    if winner:
        print(f"{winner} wins!")
        break
    if is_board_full():
        print("It's a draw!")
        break

    print("Computer's turn...")
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            break
    print_board()

    winner = check_winner()
    if winner:
        print(f"{winner} wins!")
        break
    if is_board_full():
        print("It's a draw!")
        break