from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    min_val = inf
    max_profit = 0
    for price in prices:
        min_val = min(min_val, price)
        max_profit = max(max_profit, price - min_val)

    return max_profit