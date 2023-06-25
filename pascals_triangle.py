from sys import *
from collections import *
from math import *


def ncr(n,r):
    ans = 1
    for i in range(r):
        ans *= (n-i)
        ans //= (i+1)
    return ans


def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    res = []
    for row in range(1, n+1):
        tmp = []
        for col in range(1, row+1):
            tmp.append(ncr(row-1, col-1))
        res.append(tmp)
    return res