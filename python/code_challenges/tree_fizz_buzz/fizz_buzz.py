from code_challenges.stack_and_queue.queue import Queue

class Node:
    def __init__(self,value):
        self.value = value
        self.children = []

def fizz_buzz(root):
    new_que = Queue()
    new_que.enqueue(root)
    while new_que.isempty != True:
        temp = new_que.dequeue()
        if temp.value%3 == 0:
            temp.value = 'Fizz'
        elif temp.value%5 == 0:
            temp.value = 'Buzz'
        elif temp.value%5 == 0 and temp.value%3 == 0:
            temp.value = 'FizzBuzz'
        else:
            temp.value = str(temp.value)
        for child in temp.children:
            new_que.enqueue(child) 
