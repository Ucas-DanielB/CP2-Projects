import csv

def load_coins(country):
    # Loads coin denominations from coins.csv for a given country
    try:
        # Opens csv file in read mode
        with open("Coin Change Problem/coins.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                # csv format 
                if row[0].strip().lower() == country.lower():
                    coins = [item.split("-") for item in row[1:]]
                    return [(name, int(value)) for name, value in coins]
        # Error messagewhen country is not inside the csv file
        print("\n Error: Country not found in the coin file. Please try again.\n")
        return None
    except FileNotFoundError:
        # Error message when there is no coin csv file
        print("\n Error: The coin file is missing. Make sure 'coins.csv' is in the program directory.\n")
        return None
