"""
Difficulty: Easy
Category: Arrays

Given an array of positive integers representing the values of coins in your possesion, write a function that return the 
minimum amount of the change (the minimum sum of money) that you cannot create. The given coins can have any positive integer
value and aren't necessarily unique (i.e., you can have multiple coins of the same value).

For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4. If you're given no coins,
the minimum amount of change that you can't create is 1.

"""

"""
tests

coins = [5, 7, 1, 1, 2, 3, 22]
"""

def non_constructible_change(coins):
    coins.sort()

    minimum_change = 0

    for coin in coins:
        if coin > minimum_change + 1:
            return minimum_change + 1
        minimum_change += coin
    return minimum_change + 1

