from code_challenges.stack_and_queue.queue import Queue

def breadth_first(root):
    final_list = []
    new_que = Queue()
    new_que.enqueue(root)

    while new_que.isempty() != True:
        temp = new_que.dequeue()
        final_list.append(temp.value)
        if temp.left is not None:
            new_que.enqueue(temp.left)
        if temp.right is not None:
            new_que.enqueue(temp.right)
    return final_list



