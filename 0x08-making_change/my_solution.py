def makeChange(coins, total):
    coins = sorted(coins, reverse=True)
    coins1 = coins[:]
    coinsStack = 0
    neededCoins = 0

    if total <= 0:
        return 0
    elif len(coins) == 1:
        if coins[0] > total:
            return -1
        return total // coins[0]

    while coinsStack < total:
        if coinsStack + coins1[0] <= total:
            coinsStack += coins1[0]
            neededCoins += 1
        else:
            coins1.pop(0)
            if len(coins1) == 0:
                break

    if coinsStack != total:
        return -1

    return neededCoins
