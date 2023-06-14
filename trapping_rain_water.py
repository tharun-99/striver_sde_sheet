from os import *
from sys import *
from collections import *
from math import *

def getTrappedWater(arr, n) :
	# Write your code here.
	left_max, right_max = arr[0], arr[n-1]
	water = 0
	l, r = 0, n-1
	while l < r:
		if left_max < right_max:
			l += 1
			if arr[l] < left_max:
				water += (left_max - arr[l])
			left_max = max(left_max, arr[l])
		else:
			r -= 1
			if arr[r] < right_max:
				water += (right_max - arr[r])
			right_max = max(right_max, arr[r])
	return water