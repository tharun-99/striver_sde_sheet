from os import *
from sys import *
from collections import *
from math import *

class Queue :

    #Define data members and __init__()

    def __init__(self):
        self.q = []

    '''----------------- Public Functions of Queue -----------------'''

   
    def isEmpty(self) :
        #Implement the isEmpty() function
        if not self.q:
            return True
        return False


    def enqueue(self, data) :
        #Implement the enqueue(element) function
        self.q.append(data)


    def dequeue(self) :
        #Implement the dequeue() function
        if self.q:
            return self.q.pop(0)
        return -1


    def front(self) :
        #Implement the front() function
        if self.q:
            return self.q[0]
        return -1
