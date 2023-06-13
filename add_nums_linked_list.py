class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    # Write your code here.
    carry = False
    new_head = Node()
    curr = new_head

    while head1 and head2:
        sum = head2.data + head1.data + (1 if carry else 0)
        if sum >= 10:
            carry = True
            sum = sum % 10
            curr.next = Node(data = sum)
            curr = curr.next
        else:
            carry = False
            curr.next = Node(data = sum)
            curr = curr.next
        head1 = head1.next
        head2 = head2.next

    while head2:
        sum = head2.data + (1 if carry else 0)
        if sum >= 10:
            carry = True
            sum = sum % 10
            curr.next = Node(data = sum)
            curr = curr.next
        else:
            carry = False
            curr.next = Node(data = sum)
            curr = curr.next
        head2 = head2.next

    while head1:
        sum = head1.data + (1 if carry else 0)
        if sum >= 10:
            carry = True
            sum = sum % 10
            curr.next = Node(data = sum)
            curr = curr.next
        else:
            carry = False
            curr.next = Node(data = sum)
            curr = curr.next
        head1 = head1.next

    if carry:
        curr.next = Node(data = 1)
        curr = curr.next
        
    return new_head.next

