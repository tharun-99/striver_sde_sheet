from sys import *
from collections import *
from math import *

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    arr.sort()
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            return int(arr[i])