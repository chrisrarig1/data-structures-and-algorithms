from code_challenges.stack_and_queue.node import Node
import sys


class Stack:
        def __init__(self, top=None):
            self.top = top

        def push(self, value):
            node = Node(value)
            if self.top == None:
                node.next = None
            else:
                node.next = self.top
            self.top = node

        
        def pop(self):
            try:
                temp = Node(self.top)
                self.top = self.top.next
                temp.next = None
                return temp.value
            except AttributeError:
                return('empty stack')
        
        
        def peek(self):
            try:
                return self.top.value
            except AttributeError:
                return('empty stack')
        
        def empty(self):
            return self.top == None





