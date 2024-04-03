class Node:
    def __init__(self, containers):
        self.containers = containers
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.insertion_order = []

    def insert(self, containers):
        if not self.root:
            self.root = Node(containers)
            self.insertion_order.append(self.root)
        else:
            self._insert(containers, self.root)

    def _insert(self, containers, node):
        if containers < node.containers:
            if not node.left:
                node.left = Node(containers)
                self.insertion_order.append(node.left)
            else:
                self._insert(containers, node.left)
        else:
            if not node.right:
                node.right = Node(containers)
                self.insertion_order.append(node.right)
            else:
                self._insert(containers, node.right)

    def inorder_traversal(self):
        for node in self.insertion_order:
            print(node.containers, end=' ')

# Example usage:
tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(80)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(90)

print("Number of shipping containers on each boat (in order of insertion):")
tree.inorder_traversal()


