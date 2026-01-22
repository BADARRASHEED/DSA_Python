class Node:
    """
    A single node in an AVL Tree (self-balancing BST).

    Fields:
      - val:   stored key (must support < and > comparisons)
      - left:  left child
      - right: right child
      - h:     node height in NODES (leaf = 1)

    Note:
      Public BST height (in EDGES) is: (root.h - 1), and empty tree is -1.
    """

    __slots__ = ("val", "left", "right", "h")

    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.h = 1  # height in nodes


class AVL:
    """
    Production-grade AVL Tree (no imports).

    Duplicate policy:
      - "right"  : equal keys go to right subtree
      - "left"   : equal keys go to left subtree
      - "reject" : duplicates not allowed (raises ValueError on insert)

    Guarantees:
      - Search / insert / delete are O(log n) due to AVL rebalancing.
    """

    def __init__(self, iterable=None, duplicates="right"):
        if duplicates not in ("right", "left", "reject"):
            raise ValueError("duplicates must be one of: 'right', 'left', 'reject'")

        self.root = None
        self._size = 0
        self._duplicates = duplicates

        if iterable is not None:
            for x in iterable:
                self.insert(x)

    # ---------------------------
    # Core utilities / dunders
    # ---------------------------
    def __len__(self):
        return self._size

    def size(self):
        return self._size

    def is_empty(self):
        return self.root is None

    def clear(self):
        self.root = None
        self._size = 0

    def __contains__(self, key):
        return self.contains(key)

    def __iter__(self):
        return self.inorder()

    def __repr__(self):
        return "AVL(size=%d, duplicates=%r)" % (self._size, self._duplicates)

    def __str__(self):
        return "AVL" + str(self.to_list_inorder())

    # ---------------------------
    # Height helpers (node height = nodes)
    # ---------------------------
    def _h(self, node):
        return 0 if node is None else node.h

    def _update_h(self, node):
        lh = self._h(node.left)
        rh = self._h(node.right)
        node.h = 1 + (lh if lh > rh else rh)

    def _balance_factor(self, node):
        return self._h(node.left) - self._h(node.right)

    # ---------------------------
    # Rotations
    # ---------------------------
    def _rotate_right(self, y):
        #      y              x
        #     / \            / \
        #    x   T3   =>    T1  y
        #   / \                / \
        #  T1  T2             T2  T3
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        self._update_h(y)
        self._update_h(x)
        return x

    def _rotate_left(self, x):
        #    x                 y
        #   / \               / \
        #  T1  y     =>      x  T3
        #     / \           / \
        #    T2 T3         T1 T2
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        self._update_h(x)
        self._update_h(y)
        return y

    def _rebalance(self, node):
        """Rebalance a node after insertion/deletion. Returns new subtree root."""
        if node is None:
            return None

        self._update_h(node)
        bf = self._balance_factor(node)

        if bf > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if bf < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # ---------------------------
    # Comparison direction (handles duplicates policy)
    # ---------------------------
    def _dir(self, key, node_val):
        """
        Returns:
          -1 if key should go left
           0 if key equals node_val
          +1 if key should go right
        """
        if key < node_val:
            return -1
        if key > node_val:
            return 1
        return 0

    # ---------------------------
    # Search / Get
    # ---------------------------
    def search(self, key):
        """Return the Node containing key, or None if not found."""
        cur = self.root
        while cur is not None:
            d = self._dir(key, cur.val)
            if d == 0:
                return cur
            cur = cur.left if d < 0 else cur.right
        return None

    def contains(self, key):
        return self.search(key) is not None

    def get(self, key, default=None):
        n = self.search(key)
        return default if n is None else n.val

    # ---------------------------
    # Insert / Extend
    # ---------------------------
    def insert(self, key):
        """
        Insert key into AVL.

        duplicates:
          - "right": equals go right
          - "left" : equals go left
          - "reject": raise ValueError if key exists
        """
        inserted = [False]  # mutable flag (no imports)
        self.root = self._insert_rec(self.root, key, inserted)
        if inserted[0]:
            self._size += 1
        return inserted[0]

    def _insert_rec(self, node, key, inserted):
        if node is None:
            inserted[0] = True
            return Node(key)

        d = self._dir(key, node.val)

        if d == 0:
            if self._duplicates == "reject":
                raise ValueError("Duplicate key rejected by policy")
            if self._duplicates == "left":
                node.left = self._insert_rec(node.left, key, inserted)
            else:  # "right"
                node.right = self._insert_rec(node.right, key, inserted)
        elif d < 0:
            node.left = self._insert_rec(node.left, key, inserted)
        else:
            node.right = self._insert_rec(node.right, key, inserted)

        return self._rebalance(node)

    def extend(self, iterable):
        for x in iterable:
            self.insert(x)

    # ---------------------------
    # Min / Max (values + nodes)
    # ---------------------------
    def _min_node(self, node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur

    def _max_node(self, node):
        cur = node
        while cur.right is not None:
            cur = cur.right
        return cur

    def min_value(self):
        if self.root is None:
            raise ValueError("AVL is empty")
        return self._min_node(self.root).val

    def max_value(self):
        if self.root is None:
            raise ValueError("AVL is empty")
        return self._max_node(self.root).val

    def min_node(self):
        return None if self.root is None else self._min_node(self.root)

    def max_node(self):
        return None if self.root is None else self._max_node(self.root)

    # ---------------------------
    # Delete (AVL rebalancing)
    # ---------------------------
    def delete(self, key):
        """
        Delete ONE occurrence of key.
        Returns True if deleted, else False.
        """
        deleted = [False]
        self.root = self._delete_rec(self.root, key, deleted)
        if deleted[0]:
            self._size -= 1
        return deleted[0]

    def _pop_min(self, node):
        """
        Remove the minimum node from the given subtree and return a tuple:
            (min_value, new_subtree_root)

        This is duplicates-safe: it removes the exact leftmost node, not just "a value".
        """
        if node.left is None:
            # node itself is the minimum; remove it by returning its right child
            return node.val, node.right

        min_val, node.left = self._pop_min(node.left)
        return min_val, self._rebalance(node)

    def _delete_rec(self, node, key, deleted):
        if node is None:
            return None

        d = self._dir(key, node.val)

        if d < 0:
            node.left = self._delete_rec(node.left, key, deleted)
        elif d > 0:
            node.right = self._delete_rec(node.right, key, deleted)
        else:
            # Found a node to delete
            deleted[0] = True

            # 0 or 1 child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # 2 children: replace with inorder successor (exact node removal)
            min_val, node.right = self._pop_min(node.right)
            node.val = min_val
        return self._rebalance(node)

    def delete_all(self, key):
        count = 0
        while self.delete(key):
            count += 1
        return count

    # ---------------------------
    # Pop min / max (delete + return)
    # ---------------------------
    def pop_min(self):
        """Remove and return the minimum value (single pass)."""
        if self.root is None:
            raise ValueError("AVL is empty")
        v, self.root = self._pop_min(self.root)
        self._size -= 1
        return v

    def _pop_max(self, node):
        """Remove max node from subtree and return (max_value, new_subtree_root)."""
        if node.right is None:
            return node.val, node.left
        max_val, node.right = self._pop_max(node.right)
        return max_val, self._rebalance(node)

    def pop_max(self):
        """Remove and return the maximum value (single pass)."""
        if self.root is None:
            raise ValueError("AVL is empty")
        v, self.root = self._pop_max(self.root)
        self._size -= 1
        return v

    # ---------------------------
    # Height (edges)
    # ---------------------------
    def height(self):
        """
        Height in EDGES:
          - empty tree -> -1
          - single node -> 0
        """
        return -1 if self.root is None else (self.root.h - 1)

    # ---------------------------
    # Traversals (generators)
    # ---------------------------
    def inorder(self):
        """Iterative inorder (sorted order)."""
        stack = []
        cur = self.root
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            yield cur.val
            cur = cur.right

    def preorder(self):
        """Iterative preorder (root-left-right)."""
        if self.root is None:
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            yield node.val
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    def postorder(self):
        """Iterative postorder (left-right-root)."""
        if self.root is None:
            return
        s1 = [self.root]
        s2 = []
        while s1:
            node = s1.pop()
            s2.append(node)
            if node.left is not None:
                s1.append(node.left)
            if node.right is not None:
                s1.append(node.right)
        while s2:
            yield s2.pop().val

    def levelorder(self):
        """Breadth-first traversal (queue via list + index)."""
        if self.root is None:
            return
        q = [self.root]
        i = 0
        while i < len(q):
            node = q[i]
            i += 1
            yield node.val
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    # ---------------------------
    # Range query (sorted + early break)
    # ---------------------------
    def range_query(self, lo, hi):
        """
        Return a sorted list of values x such that:
            lo <= x <= hi
        """
        if lo > hi:
            return []

        out = []
        for v in self.inorder():
            if v < lo:
                continue
            if v > hi:
                break
            out.append(v)
        return out

    # ---------------------------
    # Kth smallest
    # ---------------------------
    def kth_smallest(self, k):
        """1-indexed: kth_smallest(1) is minimum."""
        if not isinstance(k, int):
            raise TypeError("k must be int")
        if k <= 0 or k > self._size:
            raise ValueError("k out of range")

        count = 0
        for v in self.inorder():
            count += 1
            if count == k:
                return v
        raise ValueError("k out of range")

    # ---------------------------
    # Duplicates support
    # ---------------------------
    def count(self, key):
        """
        Count occurrences of key.
        This counts by walking along the side where duplicates are chained by policy.
        """
        c = 0
        cur = self.root
        while cur is not None:
            d = self._dir(key, cur.val)
            if d == 0:
                c += 1
                cur = cur.left if self._duplicates == "left" else cur.right
            elif d < 0:
                cur = cur.left
            else:
                cur = cur.right
        return c

    # ---------------------------
    # Successor / Predecessor
    # ---------------------------
    def successor(self, key):
        """
        Return the next greater value after key, or None if no successor.
        Works even if key is not present (insertion-point successor).
        """
        cur = self.root
        succ = None
        while cur is not None:
            if key < cur.val:
                succ = cur
                cur = cur.left
            else:
                cur = cur.right
        return None if succ is None else succ.val

    def predecessor(self, key):
        """
        Return the previous smaller value before key, or None if no predecessor.
        Works even if key is not present (insertion-point predecessor).
        """
        cur = self.root
        pred = None
        while cur is not None:
            if key > cur.val:
                pred = cur
                cur = cur.right
            else:
                cur = cur.left
        return None if pred is None else pred.val

    # ---------------------------
    # Validation / Sanity checks
    # ---------------------------
    def validate_size(self):
        count = 0
        for _ in self.inorder():
            count += 1
        return count == self._size

    def is_bst(self):
        """
        Validate sorted-order property via inorder monotonicity.
        Note: This validates BST ordering, not duplicates placement side.
        """
        prev_set = False
        prev = None
        for v in self.inorder():
            if not prev_set:
                prev = v
                prev_set = True
                continue
            if self._duplicates == "reject":
                if v <= prev:
                    return False
            else:
                if v < prev:
                    return False
            prev = v
        return True

    def is_avl(self):
        """
        Validate:
          - BST ordering
          - AVL balance condition: |bf(node)| <= 1 for all nodes
          - stored heights are consistent
        """
        if not self.is_bst():
            return False
        ok, _ = self._check_avl(self.root)
        return ok

    def _check_avl(self, node):
        if node is None:
            return True, 0  # ok, height(nodes)=0

        ok_l, hl = self._check_avl(node.left)
        if not ok_l:
            return False, 0

        ok_r, hr = self._check_avl(node.right)
        if not ok_r:
            return False, 0

        # height consistency
        expected_h = 1 + (hl if hl > hr else hr)
        if node.h != expected_h:
            return False, 0

        # balance factor
        bf = hl - hr
        if bf < -1 or bf > 1:
            return False, 0

        return True, expected_h

    # ---------------------------
    # Convenience
    # ---------------------------
    def to_list_inorder(self):
        return [v for v in self.inorder()]


# Example usage:
if __name__ == "__main__":
    avl = AVL([5, 3, 7, 2, 4, 6, 8, 4, 4], duplicates="right")

    print("Inorder:", avl.to_list_inorder())
    print("Size:", len(avl), "| validate_size:", avl.validate_size())
    print("Min:", avl.min_value(), "| Max:", avl.max_value())
    print("Height:", avl.height())
    print("Count(4):", avl.count(4))
    print("Successor(4):", avl.successor(4))
    print("Predecessor(4):", avl.predecessor(4))
    print("Range [4,7]:", avl.range_query(4, 7))
    print("k=3:", avl.kth_smallest(3))

    print("pop_min:", avl.pop_min())
    print("pop_max:", avl.pop_max())
    print("After pops inorder:", avl.to_list_inorder())

    avl.delete(3)
    print("After delete 3 inorder:", avl.to_list_inorder())
    print("Is BST:", avl.is_bst())
    print("Is AVL:", avl.is_avl())
