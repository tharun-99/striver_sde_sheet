'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def removeKthNode(head, k):
    # Write your code here.
    # 1 -> 2 -> 3 -> 4 -> 5
    if not head:
        return head

    slow, fast = head, head
    while k:
        fast = fast.next
        k -= 1
    if fast is None:
        return slow.next
    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head
