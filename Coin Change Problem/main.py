# Daniel Blanco, coin change problem

from coin_handler import load_coins
from coin_change import get_min_coins

def main():
    print("===  Coin Change Solver ===\n")
    
    while True:
        country = input("Enter the country (USA, UK, Canada, Euro): ").strip()
        coins = load_coins(country)

        if coins:
            break  # Proceed if a valid country was entered

    while True:
        try:
            target = int(input("\nEnter the target amount in cents: ").strip())
            if target <= 0:
                print(" Error: Target amount must be a positive integer. Try again.")
            else:
                break
        except ValueError:
            print(" Error: Invalid input. Please enter a numerical value.")

    min_coins, coin_breakdown = get_min_coins(target, coins)

    if min_coins is None:
        print("\n Error: Cannot make exact change with available coins.\n")
    else:
        print(f"\n Minimum coins needed: {min_coins}")
        print(" Coins used:")
        for name, count in coin_breakdown.items():
            print(f"  {name}: {count}")

if __name__ == "__main__":
    main()
