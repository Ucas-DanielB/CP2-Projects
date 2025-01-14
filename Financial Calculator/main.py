# Import necessary modules
import math

# Function to calculate the time required to save for a goal
def time_to_save(goal_amount, deposit_amount, frequency):
    if deposit_amount <= 0:
        return "Deposit amount must be greater than zero."
    periods = math.ceil(goal_amount / deposit_amount)
    return periods if frequency.lower() == 'weekly' else periods // 4

# Compound interest calculator
def compound_interest(principal, rate, times_compounded, years):
    if principal < 0 or rate < 0 or times_compounded <= 0 or years < 0:
        return "Invalid inputs. Ensure values are positive."
    return principal * (1 + rate / (100 * times_compounded))**(times_compounded * years)

# Budget allocator
def budget_allocator(income, percentages):
    allocation = {}
    for category, percentage in percentages.items():
        allocation[category] = income * (percentage / 100)
    return allocation

# Sale price calculator
def sale_price(original_price, discount_percent):
    if original_price < 0 or discount_percent < 0 or discount_percent > 100:
        return "Invalid inputs for sale price."
    return original_price * (1 - discount_percent / 100)

# Tip calculator
def calculate_tip(bill_amount, tip_percent):
    if bill_amount < 0 or tip_percent < 0:
        return "Invalid inputs for tip."
    return bill_amount * (tip_percent / 100)

# Main function to run the user interface
def main():
    while True:
        print("\nChoose an option:")
        print("1. Time to Save")
        print("2. Compound Interest Calculator")
        print("3. Budget Allocator")
        print("4. Sale Price Calculator")
        print("5. Tip Calculator")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            goal = float(input("Enter the savings goal amount: "))
            deposit = float(input("Enter the weekly/monthly deposit amount: "))
            frequency = input("Is this deposit weekly or monthly? ").strip().lower()
            result = time_to_save(goal, deposit, frequency)
            print(f"Time to save: {result} {frequency}s")
        elif choice == "2":
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the annual interest rate (in %): "))
            times = int(input("Enter the number of times interest is compounded annually: "))
            years = float(input("Enter the number of years: "))
            result = compound_interest(principal, rate, times, years)
            print(f"Compound interest result: {result}")
        elif choice == "3":
            income = float(input("Enter your total income: "))
            print("Enter budget allocation percentages for categories (e.g., savings, food):")
            categories = {}
            while True:
                category = input("Category name (or type 'done' to finish): ").strip()
                if category.lower() == 'done':
                    break
                percentage = float(input(f"Enter percentage for {category}: "))
                categories[category] = percentage
            result = budget_allocator(income, categories)
            print("Budget Allocation:")
            for cat, amount in result.items():
                print(f"{cat}: {amount:.2f}")
        elif choice == "4":
            original_price = float(input("Enter the original price: "))
            discount_percent = float(input("Enter the discount percentage: "))
            result = sale_price(original_price, discount_percent)
            print(f"Sale price: {result:.2f}")
        elif choice == "5":
            bill_amount = float(input("Enter the bill amount: "))
            tip_percent = float(input("Enter the tip percentage: "))
            result = calculate_tip(bill_amount, tip_percent)
            print(f"Tip amount: {result:.2f}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
