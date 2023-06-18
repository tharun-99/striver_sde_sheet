'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def findIntersection(firstHead, secondHead):
	# Write your code here.
    tmp1 = firstHead
    tmp2 = secondHead

    while tmp1 != tmp2:
        tmp1 = secondHead if tmp1 is None else tmp1.next
        tmp2 = firstHead if tmp2 is None else tmp2.next
    return tmp1