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

def getPreOrderTraversal(root):
    # Write your code here.
	res = []
	def preorder(root):
		if not root:
			return
		res.append(root.data)
		preorder(root.left)
		preorder(root.right)
	preorder(root)
	return res
