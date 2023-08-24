#!/usr/bin/python3
"""This is a module that is aimed
at providing a solution to the Making Change Problem
"""


def makeChange(coins, total):
    """
    The function makeChange takes two arguments:

    coins: A list of coin denominations available for making change.
    total: The total amount for which you want to make change.

    It then tries to determining the fewest number of coins
    needed to make change for a given total amount.

    """
    if total <= 0:
        return 0

    # keeps track of the total amount of change made so far
    current_total = 0
    # keeps track of the number of coins used.
    used_coins = 0

    # sort the list of coins in reverse (Greedy Algorithm)
    coins = sorted(coins, reverse=True)

    for coin in coins:
        r = (total - current_total) // coin
        current_total += r * coin
        used_coins += r
        if current_total == total:
            return used_coins
    return -1
