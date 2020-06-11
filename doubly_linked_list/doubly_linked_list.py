class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_head = ListNode(value)
        self.length += 1
        if self.length == 1:
            self.tail = new_head
        else:
            self.head.prev = new_head
            new_head.next = self.head
        self.head = new_head

    def remove_from_head(self):
        if self.length == 0:
            return None
        self.length -= 1
        old_head_value = self.head.value
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        return old_head_value

    def add_to_tail(self, value):
        new_tail = ListNode(value)
        self.length += 1
        if self.length == 1:
            self.head = new_tail
        else:
            self.tail.next = new_tail
            new_tail.prev = self.tail
        self.tail = new_tail

    def remove_from_tail(self):
        if self.length == 0:
            return None
        self.length -= 1
        old_tail_value = self.tail.value
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return old_tail_value

    def move_to_front(self, node):
        if node is self.head:
            return
        if node is self.tail:
            self.tail = self.tail.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def move_to_end(self, node):
        if node is self.tail:
            return
        if node is self.head:
            self.head = self.head.next
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

    def delete(self, node):
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
        elif node is self.tail:
            self.tail = self.tail.prev
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

    def get_max(self):
        max_val = float('-inf')
        cur_node = self.head
        while cur_node:
            if cur_node.value > max_val:
                max_val = cur_node.value
            cur_node = cur_node.next
        return max_val
