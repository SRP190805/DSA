Sure, here is a markdown file about AVL Trees:

## AVL Trees

AVL Trees are a self-balancing type of Binary Search Tree named after Georgy Adelson-Velsky and Evgenii Landis, who invented them in 1962.

### Key Points

* AVL Trees are self-balancing, meaning they keep their height to a minimum to guarantee fast runtime for searching, inserting, and deleting nodes.
* The only difference between a regular Binary Search Tree and an AVL Tree is that AVL Trees perform rotation operations to maintain balance.
* A Binary Search Tree is balanced when the difference in height between the left and right subtrees is less than 2.

### Balance Factors

A node's balance factor is the difference in heights between its right and left subtrees. The subtree heights are stored at each node for all nodes in an AVL Tree, and the balance factor is calculated based on these subtree heights to check if the tree has become unbalanced.

* The height of a subtree is the number of edges between the root node of the subtree and the leaf node farthest down in that subtree.
* The Balance Factor (BF) for a node (X) is the difference in height between its right and left subtrees:
  * BF(X) = height(rightSubtree(X)) - height(leftSubtree(X))

* Balance factor values:
    * 0: The node is balanced.
    * More than 0: The node is "right heavy".
    * Less than 0: The node is "left heavy".

If the balance factor is less than -1 or more than 1 for one or more nodes in the tree, the tree is considered unbalanced, and a rotation operation is needed to restore balance.

### Rotations

To restore balance in an AVL Tree, left or right rotations, or a combination of left and right rotations, are performed.

* Left Rotation: A single left rotation at the unbalanced node is enough to restore balance in the Right-Right (RR) case.
* Right Rotation: A single right rotation on the unbalanced node is enough to restore balance in the Left-Left (LL) case.
* Left-Right Rotation: A left rotation is done on the left child node, followed by a right rotation on the unbalanced node, to restore balance in the Left-Right (LR) case.
* Right-Left Rotation: A right rotation is done on the right child node, followed by a left rotation on the unbalanced node, to restore balance in the Right-Left (RL) case. 

### Time Complexity

The time complexity for search, insert, and delete operations on an AVL Tree is O(log n), which is significantly faster than the O(n) time complexity for unbalanced Binary Search Trees. This is because the height of an AVL Tree is guaranteed to be logarithmic in the number of nodes, even in the worst case.

I hope this markdown file is helpful!
