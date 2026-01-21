class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeTraversal:
    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.value] + self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return []
        return [root.value] + self.preorder(root.left) + self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.value]


# Example usage:
if __name__ == "__main__":
    # Creating a sample tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    traversal = TreeTraversal()
    print("Inorder traversal:", traversal.inorder(root))
    print("Preorder traversal:", traversal.preorder(root))
    print("Postorder traversal:", traversal.postorder(root))
