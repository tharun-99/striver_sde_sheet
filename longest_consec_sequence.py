from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    s = set()
    for num in arr:
        s.add(num)
    
    longest = 1
    for num in arr:
        if num-1 not in s:
            curr = 0
            tmp = num
            while tmp in s:
                curr += 1
                tmp += 1
            longest = max(longest, curr)
    return longest
