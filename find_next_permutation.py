from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    # Write your code here.
    # Return a list.
    next_small = -1
    for i in range(n-2, -1, -1):
        if permutation[i] < permutation[i+1]:
            next_small = i
            break
    if next_small == -1:
        return permutation[::-1]
    
    next_big = -1
    min_big = 10**6

    for i in range(next_small+1, n):
        if permutation[i] > permutation[next_small]:
            if permutation[i] < min_big:
                min_big = permutation[i]
                next_big = i

    permutation[next_small], permutation[next_big] = permutation[next_big], permutation[next_small]
    permutation = permutation[:next_small+1].copy() + permutation[next_small+1:][::-1].copy()
    return permutation