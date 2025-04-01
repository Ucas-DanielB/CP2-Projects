# Daniel Blanco, coin change problem

from coin_handler import load_coins
from coin_change import get_min_coins

# The main menu for the Coin change problem
def main():
    print("===  Coin Change Problem ===\n")
    
    while True: # User must input a country listed
        country = input("Enter the country (USA, UK, Canada, Euro): ").strip()
        coins = load_coins(country)

        if coins:
            break  # Proceed if a valid country was entered

    while True:
        try:
            # input for user to enter a specific amount of cents
            target = int(input("\nEnter the target amount in cents: ").strip())
            if target <= 0:
                # Error message when user inputs a negative number
                print(" Error: Target amount must be a positive integer. Try again.")
            else:
                break
        except ValueError:
            # Error message when user does not input a number
            print(" Error: Invalid input. Please enter a numerical value.")

    min_coins, coin_breakdown = get_min_coins(target, coins)

    if min_coins is None:
        # Error message
        print("\n Error: Cannot make exact change with available coins.\n")
    else:
        print(f"\n Minimum coins needed: {min_coins}")
        print(" Coins used:")
        for name, count in coin_breakdown.items():
            print(f"  {name}: {count}")

if __name__ == "__main__":
    main()
