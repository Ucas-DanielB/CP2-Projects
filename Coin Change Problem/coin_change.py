def get_min_coins(target, coins):
    #Finds the minimum number of coins to make the target amount.
    coins.sort(key=lambda x: x[1], reverse=True)  # Sort coins by value (descending)
    
    coin_count = {}  # Dictionary to store coin breakdown
    total_coins = 0
    
    for name, value in coins:
        if target >= value:
            count = target // value
            target -= count * value
            coin_count[name] = count
            total_coins += count

    if target > 0:
        return None, None  # Change cannot be made with given denominations

    return total_coins, coin_count
