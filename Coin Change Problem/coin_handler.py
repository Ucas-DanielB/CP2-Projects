import csv

def load_coins(country):
    #Loads coin denominations from coins.csv for a given country.
    try:
        # opens the coins csv page which has the currency for all the country in coins
        with open("coins.csv", "r") as file: # Opens in read mode
            reader = csv.reader(file)
            for row in reader:
                # csv file format
                if row[0].lower() == country.lower():
                    coins = [item.split("-") for item in row[1:]]
                    return [(name, int(value)) for name, value in coins]
        # Error message, invalid country in the coin file
        print("Error: Country not found in the coin file.")
        return None
    except FileNotFoundError:
        # Erorr message, appears if the csv file is not there
        print("Error: The coin file is missing.")
        return None
