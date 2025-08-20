# Hash Table with Quadratic Probing (i^2) and Auto-Rehash at load > 0.7
# Storage uses parallel lists; no built-in dicts are used.

class HashTable:
    _EMPTY = 0
    _FILLED = 1
    _TOMB  = 2

    def __init__(self, initial_capacity=11):
        # Use a prime capacity to improve probe coverage
        self.capacity = self._next_prime(max(11, initial_capacity))
        self.keys   = [None] * self.capacity
        self.values = [None] * self.capacity
        self.state  = [self._EMPTY] * self.capacity
        self.size = 0  # number of FILLED entries (excludes tombstones)

    # ---------- Public API ----------
    def insert(self, key, value):
        """Insert or update key -> value. Rehashes when load factor exceeds 0.7."""
        if self._load_factor() > 0.7:
            self._resize(self._next_prime(self.capacity * 2))

        idx, found = self._find_slot(key, for_insert=True)
        if found:
            # key already exists; update value
            self.values[idx] = value
            return

        # insert new key
        self.keys[idx] = key
        self.values[idx] = value
        self.state[idx] = self._FILLED
        self.size += 1

    def search(self, key):
        """Return value for key; raise KeyError if not found."""
        idx, found = self._find_slot(key, for_insert=False)
        if not found:
            raise KeyError(f"Key not found: {key}")
        return self.values[idx]

    def delete(self, key):
        """Delete key; raise KeyError if not found."""
        idx, found = self._find_slot(key, for_insert=False)
        if not found:
            raise KeyError(f"Key not found: {key}")
        # Mark as tombstone; keep chain intact
        self.state[idx] = self._TOMB
        self.keys[idx] = None
        self.values[idx] = None
        self.size -= 1
        # Optional: shrink/rehash policy could be added here

    # ---------- Internals ----------
    def _hash(self, key):
        # Ensure non-negative and reduce modulo capacity
        return (hash(key) & 0x7fffffff) % self.capacity

    def _load_factor(self):
        return self.size / self.capacity

    def _find_slot(self, key, for_insert):
        """
        Quadratic probing to locate a slot for key.
        Returns (index, found_bool).
        - If for_insert=True: returns the index where to insert (either empty or first tombstone),
          found_bool=True if key already exists (then index is its position).
        - If for_insert=False: returns the index where key is found; found_bool=False if absent.
        """
        start = self._hash(key)
        first_tomb = None

        for i in range(self.capacity):
            idx = (start + i * i) % self.capacity
            st = self.state[idx]

            if st == self._EMPTY:
                if for_insert:
                    # If we saw a tombstone, reuse it; otherwise use this empty
                    return (first_tomb if first_tomb is not None else idx), False
                else:
                    # search miss ends on empty
                    return idx, False

            if st == self._TOMB:
                # remember first tombstone for potential insertion
                if for_insert and first_tomb is None:
                    first_tomb = idx
                # keep probing
            else:  # _FILLED
                if self.keys[idx] == key:
                    return idx, True
                # else keep probing

        # Table should never be completely full due to rehash policy;
        # but if we get here, we must rehash and try again (defensive).
        if for_insert:
            self._resize(self._next_prime(self.capacity * 2))
            return self._find_slot(key, for_insert=True)
        return -1, False  # not found

    def _resize(self, new_capacity):
        old_keys = self.keys
        old_vals = self.values
        old_state = self.state

        self.capacity = new_capacity
        self.keys   = [None] * self.capacity
        self.values = [None] * self.capacity
        self.state  = [self._EMPTY] * self.capacity
        self.size = 0

        for i, st in enumerate(old_state):
            if st == self._FILLED:
                self.insert(old_keys[i], old_vals[i])

    # ---------- Prime utilities for capacity ----------
    @staticmethod
    def _is_prime(n):
        if n < 2: return False
        if n % 2 == 0: return n == 2
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    @classmethod
    def _next_prime(cls, n):
        if n <= 2: return 2
        if n % 2 == 0: n += 1
        while not cls._is_prime(n):
            n += 2
        return n

    # ---------- Convenience ----------
    def __len__(self):
        return self.size

    def __contains__(self, key):
        _, found = self._find_slot(key, for_insert=False)
        return found

    def __repr__(self):
        pairs = []
        for i in range(self.capacity):
            if self.state[i] == self._FILLED:
                pairs.append(f"{self.keys[i]}:{self.values[i]}")
        return "{" + ", ".join(pairs) + f"}} size={self.size}, cap={self.capacity}"


# ---------------- Demo ----------------
if __name__ == "__main__":
    ht = HashTable(initial_capacity=7)

    # Insert some pairs; updates included
    for k, v in [("Alice", 31), ("Bob", 22), ("Carol", 45), ("Dave", 18),
                 ("Eve", 29), ("Frank", 34), ("Grace", 27)]:
        ht.insert(k, v)
    ht.insert("Bob", 23)  # update

    # Search
    print("Bob ->", ht.search("Bob"))
    print("Eve ->", ht.search("Eve"))

    # Delete and try searching again
    ht.delete("Carol")
    try:
        print("Carol ->", ht.search("Carol"))
    except KeyError as e:
        print("Search after delete:", e)

    # Show that probing across tombstones still finds keys
    print("Contains Dave?", "Dave" in ht)

    # Force more insertions to trigger rehashing (>0.7 load)
    for k, v in [("Heidi", 40), ("Ivan", 50), ("Judy", 60), ("Mallory", 70)]:
        ht.insert(k, v)

    # Inspect table
    print("Table size:", len(ht), "Capacity:", ht.capacity)
    print("Alice ->", ht.search("Alice"))
    print("Judy  ->", ht.search("Judy"))
