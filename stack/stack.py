"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = None

    def __len__(self):
        return self.size

    def push(self, value):
        new_head = Node(value)
        if self.storage:
            new_head.next = self.storage
        self.storage = new_head
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        popped_value = self.storage.value
        self.storage = self.storage.next
        return popped_value
