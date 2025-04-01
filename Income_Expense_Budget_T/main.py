# Daniel Blanco, income/expense and budgeting tracker, Group Project - Personal Finance Program

def main():
    while True:

        print("===  Income/Expense and Budgeting Tracker ===\n")
        print("Choose an option: (1) Manage Income & Expenses, (2) Budgeting, (3) Exit")

        choice = input("Input your choice: ").strip()

        if choice == "1":
            manage_income_expenses()
        elif choice == "2":
            manage_budgeting()
        elif choice == "3":
            print("Goodbye!")
            return
        else: #Error Mesage
            print("Invalid choice. Please enter a number between 1 and 3.")

def manage_income_expenses():
    print("Input income and expense entries: date, amount, and source/categories.")
#
#    OPEN "finance_data.csv" IN APPEND MODE
#
#    while True:
#        print("please enter the date (YYYY-MM-DD):")
#        date = input("date: ")
#        print("please enter the amount below")
#        amount = input("amount: ")
#        print("Please enter the source or category:")
#        category = input("category: ")
#
#        print("Confirm entry: " + date + ", " + amount + ", " + category)
#        confirmation = input("Is this correct? (yes/no) or type 'exit' to cancel")
#
#        if confirmation == "exit":
#            CLOSE FILE
#            return
#        
#        else: if confirmation == "yes":
#            WRITE date, amount, category TO FILE
#            print("Entry saved.")
#            CLOSE FILE
#            return 
#        
#        else:
#            print("Incorrect input. Please re-enter the details.")
#
#    CLOSE FILE
#
#    CALL display_total_income_expenses()
#
