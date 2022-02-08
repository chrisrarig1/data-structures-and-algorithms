from code_challenges.stack_and_queue.node import Node
from code_challenges.stack_and_queue.stack import Stack

class AnimalShelter():
    def __init__(self, front=None):
        self.front = front
        self.rear = None

    def enqueue(self,animal):
        if animal == 'dog' or animal == 'cat':
            node = Node(animal)
            if self.rear == None:
                self.front = node
                self.rear = self.front
            else:
                self.rear.next = node
                self.rear = node
        else:
            return 'Null'

    def dequeue(self,pref):
        temp1 = Stack()
        temp2 = Stack()
        pet = None
        if pref == 'dog' or pref == 'cat':
            while self.front:
                if self.front.value == pref and pet != pref:
                    temp = self.front
                    self.front = self.front.next
                    temp.next = None
                    pet = temp.value
                else:
                    temp = self.front
                    self.front = self.front.next
                    temp.next = None
                    temp1.push(temp.value)
            while temp1.top:
                val = temp1.pop()
                temp2.push(val.value)
            while temp2.top:
                val2 = temp2.pop()
                self.enqueue(val2.value)
                # node = Node(val2.value)
                # if self.rear == None:
                #     self.front = node
                #     self.rear = self.front
                # else:
                #     self.rear.next = node
                #     self.rear = node
        else:
            return 'Null'
        return pet