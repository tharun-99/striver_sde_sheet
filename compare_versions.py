from os import *
from sys import *
from collections import *
from math import *

def compareVersions(a, b):
    #Write your code here
    lst_a = [int(x) for x in a.split('.')]
    lst_b = [int(x) for x in b.split('.')]
    a_len = len(lst_a)
    b_len = len(lst_b)

    if a_len > b_len:
        lst_b = lst_b + [0]*(a_len - b_len)
    elif b_len > a_len:
        lst_a = lst_a + [0]*(b_len - a_len)

    for i in range(max(a_len, b_len)):
        if int(lst_b[i]) > int(lst_a[i]):
            return -1
        elif int(lst_b[i]) < int(lst_a[i]):
            return 1
    return 0