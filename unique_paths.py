from sys import *
from collections import *
from math import *

def uniquePaths(m, n):
	# Write your code here.
	matrix = [[1 for _ in range(n)] for __ in range(m)]
	for r in range(1,m):
		for c in range(1,n):
			matrix[r][c] = matrix[r-1][c] + matrix[r][c-1]
	return matrix[m-1][n-1]