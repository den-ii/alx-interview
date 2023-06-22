#!/usr/bin/python3
''' making_change module '''


def makeChange(coins, total):
    '''
     coin(args): List
     total(args): int
    '''
    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the min_coins list for each amount from coin to total
        for amount in range(coin, total + 1):
            # Choose the minimum between the
            # current min_coins[amount]
            # and min_coins[amount - coin] + 1
            min_coins[amount] = min(
                min_coins[amount], min_coins[amount - coin] + 1)

    # If the total cannot be met by any combination of coins, return -1
    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]
    # coins = sorted(coins)
    # coins.reverse()

    # coins1 = coins[0:]
    # coins2 = len(coins)
    # coinsStack = 0
    # neededCoins = 0
    # # returns 0 if total is <= 0
    # if (total <= 0):
    #     return 0
    # if coins length is 1 that me
    # we have only 1 coins we check
    # if it is decimal or int
    # elif (len(coins) == 1):
    #     if total/coins is type(bool) or coins[0] < total:
    #         return -1
    #     return total/coins

    #  while coinStack is not equal to total
    # while coinsStack != total:
    #     # print("loop")
    # check if coinstack + coins1[0] < total;
    # add it; increase needed coins
    #     if coinsStack + coins1[0] <= total:
    #         coinsStack += coins1[0]
    #         neededCoins += 1
    #     # if not we pop the first coin
    #     elif coinsStack + coins1[0] > total and len(coins1) >= 2:
    #         if len(coins1) == 2:
    #             coins1 = [coins1[1]]
    #             print(coins1)
    #         else:
    #             # elif len(coins1) > 2:
    #             coins1 = coins1[1:]
    #     # pop the list again to form a new one
    #     elif coinsStack + coins1[0] > total and
    # len(coins1) >= 1 and coins2 >= 2:
    #         # print("3rd if")
    #         coins1 = coins[1:]
    #         coins2 = coins2 - 1

    #         coinsStack = 0
    #         print(coins2)
    #         neededCoins = 0
    #     elif coinsStack + coins1[0] > total and coins2 < 2:
    #         print("last if")
    #         # break
    #         return -1
    # return neededCoins
# print(makeChange([1, 2, 25], 37))
