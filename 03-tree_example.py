# Class describing a node of tree
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v
 
# Inorder Traversal
def printInorder(root):
    if root:
        # Traverse left subtree
        printInorder(root.left)
         
        # Visit node
        print(root.data,end=" ")
         
        # Traverse right subtree
        printInorder(root.right)
 
if __name__ == "__main__":
    # Build the tree
    root = Node(45)
    root.left = Node(25)
    root.right = Node(30)
    root.left.left = Node(20)
    root.left.right = Node(35)
    root.right.left = Node(15)
    root.right.right = Node(55)
 
    # Function call 
    print("Inorder Traversal:",end=" ")
    printInorder(root)