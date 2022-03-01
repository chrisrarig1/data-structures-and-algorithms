from typing import final
from code_challenges.stack_and_queue.queue import Queue

def breadth_first(tree):
    final_list = []
    new_que = Queue()
    new_que.enqueue(tree.root)

    while new_que.isempty() == False:
        temp = new_que.dequeue()
        final_list.append(temp.value)
        if temp.left is not None:
            new_que.enqueue(temp.left)
        if temp.right is not None:
            new_que.enqueue(temp.right)
    return final_list





