from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    l, r, i = 0, n-1, 0
    while i <= r:
        if arr[i] == 0:
            arr[l], arr[i] = arr[i], arr[l]
            l += 1
            i += 1
        elif arr[i] == 2:
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
        else:
            i += 1


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
