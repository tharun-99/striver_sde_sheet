from math import *
from collections import *
from sys import *
from os import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
    ptr = m+n-1
    a1 = m-1
    a2 = n-1
    while a1 >= 0 and a2 >= 0:
        if arr1[a1] < arr2[a2]:
            arr1[ptr] = arr2[a2]
            ptr -= 1
            a2 -= 1
        else:
            arr1[ptr] = arr1[a1]
            ptr -= 1
            a1 -= 1
    if a2 >= 0:
        arr1[:a2+1] = arr2[:a2+1]
    return arr1
