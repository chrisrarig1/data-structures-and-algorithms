from code_challenges.stack_and_queue.queue import Queue


class Node:
    def __init__(self,value = None):
        self.value = value
        self.children = []

    def add_child(self, value):
        self.children.append(value)

def fizz_buzz(value):
    if value % 5 == 0 and value % 3 == 0:
        return 'FizzBuzz'
    elif value % 3 == 0:
        return 'Fizz'
    elif value % 5 == 0:
        return 'Buzz'

    else:
        return str(value)


def fizz_buzz_tree(tree):
    new_tree = Node(tree)
    new_que = Queue()
    new_que.enqueue(new_tree.value)
    while new_que.isempty() != True:
        temp = new_que.dequeue()
        fizz = fizz_buzz(temp)
        if new_tree.value == None:
            new_tree.value = fizz
        else:
            new_tree.add_child(fizz)
        for child in new_tree.children:
            new_que.enqueue(child) 
    return new_tree