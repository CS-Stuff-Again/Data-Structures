class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.length = 1 if node else 0
        self.head = node
        self.tail = node

    def add_to_tail(self, value):
        new_tail = Node(value)
        if self.length == 0:
            self.head = new_tail
        else:
            self.tail.next = new_tail
        self.tail = new_tail
        self.length += 1

    def contains(self, value):
        cur_node = self.head
        while cur_node:
            if cur_node.value == value:
                return True
            cur_node = cur_node.next
        return False

    def remove_head(self):
        if self.length == 0:
            return None
        value = self.head.value
        if self.length == 1:
            self.tail = None
        self.head = self.head.next
        self.length -= 1
        return value

    def get_max(self):
        if self.length == 0:
            return None
        max_val = float('-inf')
        cur_node = self.head
        while cur_node:
            if cur_node.value > max_val:
                max_val = cur_node.value
            cur_node = cur_node.next
        return max_val
