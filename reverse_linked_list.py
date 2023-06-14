from math import *
from collections import *
from sys import *
from os import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


*****************************************************************"""


def reverseLinkedList(head):
    # Write your code here.
    if not head:
        return
        
    prev = None
    new_head = head.next
    head.next = prev
    prev = head
    head = new_head
    while new_head:
        new_head = new_head.next
        head.next = prev
        prev = head
        head = new_head
    return prev
