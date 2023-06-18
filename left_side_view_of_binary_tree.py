from sys import *
from collections import *
from math import *

# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLeftView(root)->list:
    # Write your code here
    # Return a list
    res = []
    def left(root, level):
        if not root:
            return
        if len(res) == level:
            res.append(root.data)
        left(root.left, level + 1)
        left(root.right, level + 1)
    left(root, 0)
    return res