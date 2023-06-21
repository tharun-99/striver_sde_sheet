class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next


def rotate(head: Node, k: int) -> Node:
    # Write your code here.
    # 1 -> 2 -> 3 -> 4 -> 5
    if not head:
        return None
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    tail.next = head
    steps = length - (k%length) - 1

    curr = head
    while steps:
        curr = curr.next
        steps -= 1
    new_head = curr.next
    curr.next = None
    return new_head