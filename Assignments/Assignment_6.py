class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a node to the end (O(n))."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def __str__(self):
        return " -> ".join(map(str, self)) or "∅"

    def reverse(self):
        """Iterative in-place reverse: O(n) time, O(1) extra space."""
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next     # store next
            cur.next = prev    # reverse link
            prev = cur         # move prev forward
            cur = nxt          # move cur forward
        self.head = prev

    def reverse_recursive(self):
        def _rev(node, prev=None):
            if not node:
                return prev
            nxt = node.next
            node.next = prev
            return _rev(nxt, node)
        self.head = _rev(self.head)

ll = LinkedList()
for x in [1, 2, 3, 4, 5]:
    ll.append(x)

print("Before:", ll)   
ll.reverse()
print("After: ", ll)  