from os import *
from sys import *
from collections import *
from math import *

# Stack class.
class Stack:
    
    def __init__(self, capacity: int):
        # Write your code here.
        self.stack = []
        self.curr_capacity = 0
        self.capacity = capacity

    def push(self, num: int) -> None:
        # Write your code here.
        if self.curr_capacity < self.capacity:
            self.stack.append(num)
            self.curr_capacity += 1


    def pop(self) -> int:
        # Write your code here.
        if self.curr_capacity > 0:
            item = self.stack.pop()
            self.curr_capacity -= 1
            return item
        return -1
    
    def top(self) -> int:
        # Write your code here.
        if self.curr_capacity > 0:
            item = self.stack[-1]
            return item
        return -1
    
    def isEmpty(self) -> int:
        # Write your code here.
        if self.curr_capacity == 0:
            return 1
        return 0
    
    def isFull(self) -> int:
        # Write your code here.
        if self.curr_capacity == self.capacity:
            return 1
        return 0
