from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def getMaxWidth(root):

    # Write your code here.
    if not root:
      return 0
    q = deque()
    q.append(root)
    max_width = 0
    while q:
      level_len = len(q)
      max_width = max(max_width, level_len)
      for _ in range(level_len):
        node = q.popleft()
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
    return max_width