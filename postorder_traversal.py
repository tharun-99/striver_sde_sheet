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


def getPostOrderTraversal(root):
    # Write your code here.
    res = []
    def postorder(root):
        if not root:
            return
        postorder(root.left)
        postorder(root.right)
        res.append(root.data)
    postorder(root)
    return res
