from math import *
from collections import *
from sys import *
from os import *

# Following is the List Node Class
class LinkedListNode:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next

def deleteNode(node):
    # Write your code here.

    while node.next.next:
        node.data = node.next.data
        node = node.next
    node.data = node.next.data
    node.next = None