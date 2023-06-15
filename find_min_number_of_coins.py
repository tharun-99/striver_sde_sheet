from os import *
from sys import *
from collections import *
from math import *

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):

	# Write your code here
	i = 8
	coins = 0
	while amount and i >= 0:
		if denominations[i] > amount:
			i -= 1
			continue
		coins += amount//denominations[i]
		amount = (amount%denominations[i])
		i -= 1
	return coins