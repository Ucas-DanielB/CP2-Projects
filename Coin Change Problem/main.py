# Daniel Blanco, coin change problem


from coin_handler import load_coins
from coin_change import get_min_coins

def main(): # Main function, user is asked to enter a country, the usa, uk, canada, or the currency euro
    print("=== Coin Change Solver ===")
    
    country = input("Enter the country (USA, UK, Canada, Euro): ").strip()
    coins = load_coins(country)


    if not coins:
        return
    
    try: # input cents for country
        target = int(input("Enter the target amount in cents: ").strip())
        if target <= 0:
            # Error message, cannot be a negative number
            print("Error: Target amount must be a positive integer.")
            return
    except ValueError:
        # Error message, must only be a number
        print("Error: Invalid input. Please enter a numerical value.")
        return


    min_coins, coin_breakdown = get_min_coins(target, coins)

    if min_coins is None:
        # Error message, cannot get change with the available coins
        print("Error: Cannot make exact change with available coins.")
    else:
        print(f"\nMinimum coins needed: {min_coins}")
        print("Coins used:")
        for name, count in coin_breakdown.items():
            print(f"  {name}: {count}")


if __name__ == "__main__":
    main()