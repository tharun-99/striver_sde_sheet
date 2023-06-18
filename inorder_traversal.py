from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the Binary Tree node structure:
    class TreeNode:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''


def getInOrderTraversal(root):
    # Write your code here.
    res = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.data)
        inorder(root.right)
    inorder(root)
    return res
