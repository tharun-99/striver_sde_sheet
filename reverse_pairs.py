from os import *
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
        tmp = 0
        while i < len(arr1) and j < len(arr2): 
            if arr1[i] > arr2[j]:
                while tmp < len(arr2):
                    if arr1[i] > 2 * arr2[tmp]:
                        count += (len(arr2) - tmp)
                        break
                    else:
                        tmp += 1
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

def reversePairs(arr, n):
    # Write your code here.
    global count
    count = 0
    merge_sort(arr)
    return count
    