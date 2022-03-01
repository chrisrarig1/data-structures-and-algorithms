from code_challenges.stack_and_queue.queue import Queue


class Node:
    def __init__(self,value = None):
        self.value = value
        self.children = []

    def add_child(self, value):
        self.children.append(value)

def fizz_buzz(value):
    if value.value % 3 == 0:
        value.value = 'Fizz'
    elif value.value % 5 == 0:
        value.value = 'Buzz'
    elif value.value % 5 == 0 and value.value % 3 == 0:
        value.value = 'FizzBuzz'
    else:
        value.value = str(value.value)
    return value.value


def fizz_buzz_tree(tree):
    new_tree = Node()
    new_que = Queue()
    new_que.enqueue(tree)
    while new_que.isempty() != True:
        temp = new_que.dequeue()
        fizz = fizz_buzz(temp)
        if new_tree.value == None:
            new_tree.value = fizz
        else:
            new_tree.add_child(fizz)
        for child in tree.children:
            new_que.enqueue(child) 
    return new_tree