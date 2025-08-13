class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Standard BST insert (no duplicates handling beyond placing in right subtree)."""
        if not self.root:
            self.root = Node(key)
            return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(key)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(key)
                    return

    # Q1: findMin and findMax
    def find_min(self):
        """Return the minimum key in the BST. Raises ValueError if empty."""
        if not self.root:
            raise ValueError("BST is empty")
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.key

    def find_max(self):
        """Return the maximum key in the BST. Raises ValueError if empty."""
        if not self.root:
            raise ValueError("BST is empty")
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.key


# Q2: Check if a (binary) tree is height-balanced
def is_balanced(root):
    """
    Returns True if the tree is height-balanced:
    For every node, |height(left) - height(right)| <= 1.
    Runs in O(n) by computing height bottom-up and early-stopping on imbalance.
    """
    def check(node):
        if not node:
            return 0  # height of empty tree
        lh = check(node.left)
        if lh == -1:
            return -1
        rh = check(node.right)
        if rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    return check(root) != -1



if __name__ == "__main__":
    bst = BST()
    for x in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        bst.insert(x)

    print("Min:", bst.find_min())  # -> 1
    print("Max:", bst.find_max())  # -> 14

    # Balanced example
    print("Balanced (BST root):", is_balanced(bst.root))

    # Unbalanced example
    skewed = Node(1, right=Node(2, right=Node(3, right=Node(4))))
    print("Balanced (skewed):", is_balanced(skewed))  # -> False
