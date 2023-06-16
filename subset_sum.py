from os import *
from sys import *
from collections import *
from math import *

from typing import List

def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    sum_list = [0]
    curr_list =[0]
    for n in num:
        tmp = sum_list.copy()
        for i in range(len(sum_list)):
            tmp.append(sum_list[i] + n)
        sum_list = tmp
    sum_list.sort()
    return sum_list