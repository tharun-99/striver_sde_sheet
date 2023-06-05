from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    ROWS = len(matrix)
    COLS = len(matrix[0])

    row_set = set()
    col_set = set()

    for row in range(ROWS):
        for col in range(COLS):
            if matrix[row][col] == 0:
                row_set.add(row)
                col_set.add(col)

    for row in list(row_set):
        for c in range(0, COLS):
            matrix[row][c] = 0

    for col in list(col_set):
        for r in range(0, ROWS):
            matrix[r][col] = 0
