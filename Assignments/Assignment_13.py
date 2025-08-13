class MaxHeap:
    def __init__(self, initial=None):
        self.data = []
        if initial:
            self.data = list(initial)
            self._build_heap()

    #  index helpers (0-based) 
    def _left(self, i):  return 2 * i + 1
    def _right(self, i): return 2 * i + 2
    def _parent(self, i): return (i - 1) // 2

    #  core heapify operations 
    def _heapify_up(self, i):
        """Sift-up: fix violation by swapping with parent until heap property holds."""
        while i > 0:
            p = self._parent(i)
            if self.data[i] > self.data[p]:
                self.data[i], self.data[p] = self.data[p], self.data[i]
                i = p
            else:
                break

    def _heapify_down(self, i):
        """Sift-down: fix violation by swapping down with the larger child."""
        n = len(self.data)
        while True:
            l, r = self._left(i), self._right(i)
            largest = i
            if l < n and self.data[l] > self.data[largest]:
                largest = l
            if r < n and self.data[r] > self.data[largest]:
                largest = r
            if largest == i:
                break
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i = largest

    def _build_heap(self):
        """Bottom-up heap construction in O(n)."""
        for i in range((len(self.data) - 2) // 2, -1, -1):
            self._heapify_down(i)

    #  public API 
    def insert(self, value):
        """Push a value in O(log n)."""
        self.data.append(value)
        self._heapify_up(len(self.data) - 1)

    def pop(self):
        """Remove & return the max (root). O(log n)."""
        if not self.data:
            raise IndexError("pop from empty heap")
        # Swap root with last, pop last, then heapify down
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        top = self.data.pop()
        if self.data:
            self._heapify_down(0)
        return top

    def peek(self):
        if not self.data:
            raise IndexError("peek from empty heap")
        return self.data[0]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"MaxHeap({self.data})"


#  insert then pop to show descending order 
if __name__ == "__main__":
    nums = [12, 3, 17, 8, 25, 10, 30, 15, 6]
    heap = MaxHeap()
    print("Inserting:", nums)
    for x in nums:
        heap.insert(x)

    descending = []
    while len(heap) > 0:
        descending.append(heap.pop())

    print("Popped in descending order:", descending)
    # Example output (descending):
    # [30, 25, 17, 15, 12, 10, 8, 6, 3]
