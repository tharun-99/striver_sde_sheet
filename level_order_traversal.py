from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)


#   Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def getLevelOrder(root):

    #   Write your code here
    res = []
    if not root:
        return res

    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res
    







































#   Fast input
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root


def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# main
T = int(stdin.readline().strip())
for i in range(T):
    root = takeInput()
    ans = getLevelOrder(root)
    printAns(ans)
