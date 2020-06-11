"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_head = Node(value)
        if self.head:
            new_head.next = self.head
        else:
            self.tail = new_head
        self.head = new_head
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        old_tail_value = self.tail.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            cur_node = self.head
            while cur_node.next != self.tail:
                cur_node = cur_node.next
            cur_node.next = None
            self.tail = cur_node
        return old_tail_value
