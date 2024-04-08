# Trees
## What are Trees
Trees are a data storagbe structure composed of nodes used for storing hierarchical data. Each tree node typically stores a value and references to its child nodes.

## What are the benefits of a tree node?
* It provides efficient searching, time complexity of O(log n)
* They have a flexible size, they can grow or shrink dynamically depending on the nodes that are added or removed.
* Easy to traverse, traversing a tree is a simple operation.
* Easy to maintain, Trees are easy to maintain becasue they enforce a strict hierachy and relationship between nodes.
* Natural organization, Trees have a natural hierarchical organization that can be used to represent many types of relationships
* Great for file systems and organizational structures 
* Fast insertion and deletion, inserting and deleting can be done in O(log n) time. This is very quick, even for large trees

## Disadvantages of a tree node
* Memory overhead, trees can require significant memory to store, especially if they are very large
* Imbalanced trees, if they aren't not balanced it can result in uneven search times.
* Complexity, trees can be complex data structures and can be difficult to understand
* Limited flexibility, they are flexible in terms of size and structure, they are not as flexible as some other data structures.
* Inefficient for certain operations like sorting and grouping.

## When to use
* When you need to store data and have a quick efficient recall of tha data.
* When search time matters for data retrieval

## Code to initialize a tree node
``` python

class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

```
## A tree uses the following logic 
* If the item being placed is less than the already placed item it goes to the left. 
* If it is larger than the existing item, it goes to the right.
* It continues traveling this way until it finds an open spot.
## Here is a picture of a tree node, note the letters get smaller down the left side
* the Tree = gcbaedfihjk
![Picture of a tree node](pictures\tree_nodes.png)

## Here is another example of a tree node
![Data organized in a tree node](pictures\tree_node_other.png)

## Example program using tree node
## Create a program that uses a tree to store the number of students in each class use a tree
* print out tree node in order
* store the following numbers "45 25 30 20 35 15 55"
``` python
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
```
![link to example code](tree_solution.py)

![expected output](pictures\trees_example_output.png)

## Now create your own program to store the number of shipping containers each boat holds
* use a tree node
* return the results in order they were stored
* use the following numbers for each boats storage containers 50 30 80 20 40 70 90
![link to solution code](03-tree_solution.py)

![picture of expected](pictures\tree_solution_output.png)

