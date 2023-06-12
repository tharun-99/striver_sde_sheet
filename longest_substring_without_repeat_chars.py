from os import *
from sys import *
from collections import *
from math import *

def uniqueSubstrings(input ) :
    # Write your code here.
    s = input
    dic = set()
    longest = 1
    l = 0
    for i in range(len(s)):
        if s[i] not in dic:
            dic.add(s[i])
        else:
            longest = max(longest, i-l)
            while s[i] in dic:
                dic.remove(s[l])
                l += 1
            dic.add(s[i])
    if l == 0:
        return len(s)
    longest = max(longest, i-l)
    return longest