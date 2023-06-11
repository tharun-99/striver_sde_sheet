from sys import *
from collections import *
from math import *


count = 0

def merge_sort(arr):
    global count
    if len(arr)>1:
        l = len(arr)
        mid = l//2
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        merge_sort(arr1)
        merge_sort(arr2)

        i=j=k=0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                count += (len(arr2) - j)
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1
            k += 1
        
        while i < len(arr1):
            arr[k] = arr1[i]
            i += 1
            k += 1
            
        while j < len(arr2):
            arr[k] = arr2[j]
            j += 1
            k += 1
                    
def getInversions(arr, n) :
    merge_sort(arr)
    return count

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))