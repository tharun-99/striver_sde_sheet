from math import *
from collections import *
from sys import *
from os import *

def findMajorityElement(arr, n):
	# Write your code here.
	if n == 1:
		return arr[0]
	count = 1
	num = arr[0]
	mid = n//2
	for i in range(1,n):
		if arr[i] == num:
			count += 1
		elif count == 0:
			num = arr[i]
			count = 1
		else:
			count -= 1
	
	tmp = arr.count(num)
	
	return -1 if tmp <= mid else num