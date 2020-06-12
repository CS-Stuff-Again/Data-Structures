class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.current = 0
        self.head = None
        self.tail = None
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            new_head = self.storage[key]
            if new_head is self.tail:
                self.tail = self.tail.prev
            self.head.prev = new_head
            new_head.next = self.head
            self.head = new_head
            return new_head.value[1]
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key in self.storage:
            self.storage[key].value = (key, value)
            return

        if self.current == self.limit:
            self.current -= 1
            del self.storage[self.tail.value[0]]
            self.tail = self.tail.prev
            self.tail.next = None

        self.current += 1
        new_head = Node((key, value))

        if self.head:
            self.head.prev = new_head
            new_head.next = self.head

        if not self.tail:
            self.tail = new_head

        self.head = new_head
        self.storage[key] = self.head


# lru = LRUCache(2)

# lru.set('first', 'first_value')
# lru.set('second', 'second_value')
# print(lru.get('first'))
# lru.set('third', 'third_value')

# print(lru.get('first'))
# print(lru.get('second'))
# print(lru.get('third'))
