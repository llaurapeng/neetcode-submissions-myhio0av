class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Map key to Node
        self.left, self.right = Node(0, 0), Node(0, 0)  # Dummy nodes

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node):
        """Remove a node from the doubly linked list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: Node):
        """Insert a node right before the 'right' (most recently used)."""
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        """Return the value of the key if it exists, and move it to the end (most recent)."""
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)  # Remove the node from its current position
            self.insert(node)  # Insert it as the most recently used
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Add a key-value pair to the cache. If the cache exceeds capacity, remove the least recently used item."""
        if key in self.cache:
            self.remove(self.cache[key])  # Remove the old node if exists
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)  # Insert the new node as the most recently used

        if len(self.cache) > self.capacity:
            # Remove the least recently used (LRU) node, which is the node next to 'left'
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
