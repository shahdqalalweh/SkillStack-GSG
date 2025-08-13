class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SortedCircularLinkedList:
    def __init__(self):
        self.head = None  # will always point to the smallest value

    def insert(self, x):
        new_node = Node(x)

        # Case 1: empty list
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        # Case 2: insert before current head (new smallest or equal to smallest)
        if x <= self.head.val:
            # find the tail (node whose next is head)
            tail = self.head
            while tail.next is not self.head:
                tail = tail.next
            # insert new node between tail and head, then move head
            tail.next = new_node
            new_node.next = self.head
            self.head = new_node
            return

        # Case 3: insert somewhere after head (middle or end)
        cur = self.head
        while cur.next is not self.head and cur.next.val < x:
            cur = cur.next

        new_node.next = cur.next
        cur.next = new_node

    def _iter_once(self):
        """Yield values for exactly one full cycle starting from head."""
        if not self.head:
            return
        yield self.head.val
        cur = self.head.next
        while cur is not self.head:
            yield cur.val
            cur = cur.next

    def __str__(self):
        if not self.head:
            return "[]"
        return " -> ".join(f"[{v}]" for v in self._iter_once())



if __name__ == "__main__":
    scll = SortedCircularLinkedList()
    for v in [7, 3, 9, 1, 4]:
        scll.insert(v)
        print(f"After inserting {v}: {scll}")
