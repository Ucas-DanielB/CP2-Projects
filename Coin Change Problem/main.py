# Daniel Blanco, coin change problem


from coin_handler import load_coins
from coin_change import get_min_coins

def main():
    print("=== Coin Change Solver ===")
    
    country = input("Enter the country (USA, UK, Canada, Euro): ").strip()
    coins = load_coins(country)

    if not coins:
        return
    
    try:
        target = int(input("Enter the target amount in cents: ").strip())
        if target <= 0:
            print("Error: Target amount must be a positive integer.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a numerical value.")
        return

    min_coins, coin_breakdown = get_min_coins(target, coins)

    if min_coins is None:
        print("Error: Cannot make exact change with available coins.")
    else:
        print(f"\nMinimum coins needed: {min_coins}")
        print("Coins used:")
        for name, count in coin_breakdown.items():
            print(f"  {name}: {count}")

if __name__ == "__main__":
    main()