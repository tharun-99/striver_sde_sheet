from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''
def dfs(root):
  if not root: return [0, True]
  left, l_bool = dfs(root.left)
  right, r_bool = dfs(root.right)
  tmp = 1 + max(left, right)
  tmp_bool = True if abs(left-right)<2 else False
  return [tmp, tmp_bool and l_bool and r_bool]

def isBalancedBT(root):
    # Write your code here
    # Return True/False
    return dfs(root)[1]
