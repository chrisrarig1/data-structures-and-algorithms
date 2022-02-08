import sys
def error_handle(method):
    def inner_func(*args, **kwargs):
        try:
            method(*args, **kwargs)
        except Exception as e:
                print("Yikes!", e.__class__,"occurred.")
    return inner_func

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    @error_handle
    def insert(self,value):
            node = Node(value)
            node.next = self.head
            self.head = node
    

    def includes(self,value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False 


    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result += f"{ {current.value} } -> "
            current = current.next
        else:
            result += 'NULL'
        return result

                
    def append(self,item):
        node = Node(item)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

       
    

        
    
    def insert_before(self,prior,y):
        if prior is None:
            print('error must not be null')
        if not self.includes(prior):
            print('error not in list')
        else:    
            node = Node(y)
            node.next = prior
        

    def insert_after(self,prior,y):
        if prior is None:
            print('error must not be null')
        if not self.includes(prior):
            print('error not in list')
        else:    
            node = Node(y)
            node.next = prior.next
            prior.next = node

    def kth_from_end(self,k):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        if k > length or k < 0:
            return('Exception')
        current = self.head
        for _ in range (0, length-k):
            current = current.next
        return current.value

    def reverse_string(self):
        current = self.head
        reversed_string = ""
        if current == None:
            return Exception
        while current:
            reversed_string = f'{current.value}{reversed_string}'
            current = current.next
        return reversed_string

    def zip_lists(self,ll1,ll2):
        final_list = LinkedList()
        current1 = ll1.head
        current2 = ll2.head
        while current1 or current2:
            if current1:
                final_list.append(current1.value)
                current1 = current1.next
            if current2:
                final_list.append(current2.value)
                current2 = current2.next
        return final_list

    def order(self):
        current = self.head
        pre_diff = current.value - current.next.value
        while current.next:
            temp = pre_diff
            diff = current.value - current.next.value
            if temp * diff > 0:
                current = current.next
                pre_diff = diff
            else:
                return False
        return True

class Stack:
        def __init__(self, top=None):
            self.top = top

class Queue:
        def __init__(self, front=None):
            self.front = front


if __name__ == '__main__':
    
    # print(1)
    l2 = LinkedList()
    ll = LinkedList()
    l2.insert(4)
    l2.insert(9)
    l2.insert(5)
    # l2.insert(13)
    ll.insert(3)
    ll.insert(1)
    # ll.insert(6)
    # ll.insert(3)
    print(l2)
    print(ll)
    new_list = ll.zip_lists(ll,l2)
    print(new_list)
    



    # ll.__str__()
    # ll.kth_from_end(2)
#Error Handle test
    # ll.insert()