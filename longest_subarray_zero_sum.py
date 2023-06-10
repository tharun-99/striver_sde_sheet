from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):

    # Write your Code here.
    # Return an integer denoting the answer.
    dic = {}
    dic[0] = -1
    longest = 0
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum in dic:
            longest = max(longest, i-dic[curr_sum])
        else:
            dic[curr_sum] = i
    return longest