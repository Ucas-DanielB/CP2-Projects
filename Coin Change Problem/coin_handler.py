import csv

def load_coins(country):
    """Loads coin denominations from coins.csv for a given country."""
    try:
        with open("coins.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].strip().lower() == country.lower():
                    coins = [item.split("-") for item in row[1:]]
                    return [(name, int(value)) for name, value in coins]
        print("\n Error: Country not found in the coin file. Please try again.\n")
        return None
    except FileNotFoundError:
        print("\n Error: The coin file is missing. Make sure 'coins.csv' is in the program directory.\n")
        return None
