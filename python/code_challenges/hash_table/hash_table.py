
class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class HashTable:

    def __init__(self, size=1024):
        self.size = size
        self.bucket = size * [None]

    def set(self, key, val):
        index = self.hash(key)
        newnode = Node(key,val)
        node = self.bucket[index]
        if node is None:
            self.bucket[index] = newnode
            return
        previous = node
        while node is not None:
            previous = node
            node = node.next
        previous.next = Node(key,val)
            


    def get(self,key):
        index = self.hash(key)
        node = self.bucket[index]
        while node.next is not None:
            node = node.next
        if node:
            return node.value
        else:
            return None

    def contains(self,key):
        index = self.hash(key)
        node = self.bucket[index]
        if node == None:
            return False
        while node is not None:
            if key == node.key:
                node = node.next
                return True
            else:
                node = node.next
                return False
            
        

    def keys(self):
        keys = []
        for i in self.bucket:
            if i is not None:
                keys.append(i.key)
        return keys

    def hash(self, key):
        sum = 0
        for ch in key:
           sum += ord(ch)

        primed = sum * 59
        index = primed % self.size
        return index