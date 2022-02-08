from code_challenges.stack_and_queue.node import Node
from code_challenges.stack_and_queue.stack import Stack

class PseudoQueue():
        def __init__(self):
            self.stack1 = Stack()
            self.stack2 = Stack()

        def enqueue(self,val):
            self.stack1.push(val)
            temp = self.stack1.pop()
            self.stack2.push(temp.value)

        def dequeue(self):
            try:
                deq = self.stack2.pop()
                return deq.value
            except AttributeError:
                return('empty stack')