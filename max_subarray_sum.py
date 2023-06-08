from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    max_sum, curr_sum = 0, 0
    for num in arr:
        curr_sum += num
        if curr_sum < 0:
            curr_sum = 0
        max_sum = max(max_sum, curr_sum)

    return max_sum







#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
