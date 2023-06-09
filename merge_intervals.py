from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    # Write your code here.
    intervals = sorted(intervals, key = lambda x:x[0])

    start, end = intervals[0][0], intervals[0][1]
    res = []
    for i in range(1, len(intervals)):
        curr_start, curr_end = intervals[i]
        if end < curr_start:
            res.append([start, end])
            # print("res : ", res)
            start = curr_start
            end = curr_end
        else:
            end = max(end, curr_end)
    res.append([start, end])
    # print("res ; ", res)
    return res
    

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = [arr1[i], arr2[i]]
    intervals.append(a)

res = mergeIntervals(intervals)

for i in res:
    print(i[0], i[1])
print()
