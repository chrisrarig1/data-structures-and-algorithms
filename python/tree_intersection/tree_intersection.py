from code_challenges.stack_and_queue.queue import Queue
from code_challenges.hash_table.hash_table import HashTable

def tree_intersect(tree1, tree2):
    int_arr = []
    hash_table = HashTable()
    new_que = Queue()
    new_que.enqueue(tree1.root)
    new_que2 = Queue()
    new_que2.enqueue(tree2.root)

    while new_que.isempty() == False:
        temp = new_que.dequeue()
        hash_table.set(temp.value,True)
        if temp.left is not None:
            new_que.enqueue(temp.left)
        if temp.right is not None:
            new_que.enqueue(temp.right)
    
    while new_que2.isempty() == False:
        temp = new_que2.dequeue()
        if hash_table.contains(temp.value) == True:
            int_arr.append(temp.value)
        if temp.left is not None:
            new_que2.enqueue(temp.left)
        if temp.right is not None:
            new_que2.enqueue(temp.right)
            
    return int_arr 
    
        

