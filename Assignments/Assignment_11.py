# ---------- AVL Node & Tree (insert only, for testing/demo) ----------
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_h(self, n): return n.height if n else 0
    def bf(self, n): return (self.get_h(n.left) - self.get_h(n.right)) if n else 0

    def rot_right(self, y):
        x, T2 = y.left, y.left.right
        x.right, y.left = y, T2
        y.height = 1 + max(self.get_h(y.left), self.get_h(y.right))
        x.height = 1 + max(self.get_h(x.left), self.get_h(x.right))
        return x

    def rot_left(self, x):
        y, T2 = x.right, x.right.left
        y.left, x.right = x, T2
        x.height = 1 + max(self.get_h(x.left), self.get_h(x.right))
        y.height = 1 + max(self.get_h(y.left), self.get_h(y.right))
        return y

    def _rebalance(self, node):
        balance = self.bf(node)
        if balance > 1:
            if self.bf(node.left) < 0:  # LR
                node.left = self.rot_left(node.left)
            return self.rot_right(node)   # LL
        if balance < -1:
            if self.bf(node.right) > 0:   # RL
                node.right = self.rot_right(node.right)
            return self.rot_left(node)    # RR
        return node

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.get_h(root.left), self.get_h(root.right))
        return self._rebalance(root)


# ---------- Q1) Validate AVL Tree ----------
def validate_avl(root):
    """
    Returns True iff the tree satisfies BOTH:
      1) BST property (left < node < right for all nodes)
      2) AVL balance (|height(left) - height(right)| <= 1 at every node)
    Runs in O(n).
    """
    def dfs(node):
        # Returns: (is_avl, min_key, max_key, height)
        if not node:
            return True, float('inf'), float('-inf'), 0

        L_ok, L_min, L_max, L_h = dfs(node.left)
        R_ok, R_min, R_max, R_h = dfs(node.right)

        # BST check at this node
        is_bst_here = (L_max < node.key < R_min)
        # AVL balance check at this node
        is_bal_here = abs(L_h - R_h) <= 1

        is_avl = L_ok and R_ok and is_bst_here and is_bal_here
        mn = min(L_min, node.key)
        mx = max(R_max, node.key)
        h = 1 + max(L_h, R_h)
        return is_avl, mn, mx, h

    ok, *_ = dfs(root)
    return ok


# ---------- Q2) Range Search in AVL Tree ----------
def range_search(root, low, high):
    """
    Returns a sorted list of keys in [low, high] by in-order traversal
    with pruning using BST ordering. O(m + h) where m is matches.
    """
    out = []
    def inorder(node):
        if not node:
            return
        # If node.key >= low, left subtree may contain valid keys
        if node.key >= low:
            inorder(node.left)
        # If node.key is in range, include it
        if low <= node.key <= high:
            out.append(node.key)
        # If node.key <= high, right subtree may contain valid keys
        if node.key <= high:
            inorder(node.right)
    inorder(root)
    return out


# ---------- Q3) k-th Smallest Element ----------
def kth_smallest(root, k):
    """
    Returns the k-th smallest key (1-indexed) using iterative in-order.
    Raises ValueError if k is out of bounds.
    """
    stack, cur = [], root
    count = 0
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        count += 1
        if count == k:
            return cur.key
        cur = cur.right
    raise ValueError("k is larger than the number of nodes")





if __name__ == "__main__":
    # Build sample AVL from notes: 40, 20, 60, 10, 30, 50, 70
    avl = AVLTree()
    root = None
    for x in [40, 20, 60, 10, 30, 50, 70]:
        root = avl.insert(root, x)

    # Q1: Validate AVL
    print("Is AVL? ", validate_avl(root))  # -> True

    # Q2: Range search
    print("Range [25,65]: ", range_search(root, 25, 65))  # -> [30, 40, 50, 60]

    # Another tree for Q3 demo: [50, 30, 70, 20, 40, 60, 80]
    root2 = None
    for x in [50, 30, 70, 20, 40, 60, 80]:
        root2 = avl.insert(root2, x)

    print("4th smallest: ", kth_smallest(root2, 4))  # -> 50
