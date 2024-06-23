# Depth-First Search (DFS) Traversals

DFS has three main types, each with a distinct order of visiting nodes:

1. **Pre-order:** 
    - Visit the current node.
    - Traverse the left subtree.
    - Traverse the right subtree.

2. **In-order:** 
    - Traverse the left subtree.
    - Visit the current node.
    - Traverse the right subtree.

3. **Post-order:** 
    - Traverse the left subtree.
    - Traverse the right subtree.
    - Visit the current node.
  
## Pre-order Traversal of Binary Trees

Pre-order traversal is a Depth-First Search (DFS) technique used to visit nodes in a binary tree in a specific order. You can learn more about different types of Binary Tree traversals [here](URL binary tree traversal ON Wikipedia en.wikipedia.org).

### Understanding Pre-order Traversal

Pre-order traversal follows a **Root-Left-Right** order:

1. Visit the root node (print its data).
2. Recursively perform pre-order traversal on the left subtree.
3. Recursively perform pre-order traversal on the right subtree.

This traversal is called "pre" order because the root node is visited **before** traversing its left and right subtrees.

### Pre-order Traversal in Python

Here's an example of pre-order traversal implemented in Python:

```python
def preOrderTraversal(node):
  if node is None:
    return
  print(node.data, end=", ")  # Visit the root node
  preOrderTraversal(node.left)  # Recursively traverse left subtree
  preOrderTraversal(node.right)  # Recursively traverse right subtree
```

**Explanation:**

1. The `preOrderTraversal` function takes a node as input.
2. If the node is `None` (empty), the function returns (base case).
3. If the node is not `None`, it prints the node's data followed by a comma and a space.
4. Then, it recursively calls itself on the `left` child node to perform pre-order traversal on the left subtree.
5. Finally, it recursively calls itself on the `right` child node to perform pre-order traversal on the right subtree.

**Running the Example:**

Imagine a binary tree with the following structure:

```
      R
     / \
    A   C
       / \
      B   D
```

Running the `preOrderTraversal` function on this tree will print the nodes in the following order:

```
R, A, C, B, D
```

This order reflects the pre-order visit of each node (root R), followed by its left subtree (A, B), and then its right subtree (C, D).
