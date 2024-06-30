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

## AVL Tree Out-of-Balance Cases

| Case | Description | Rotation to Restore Balance |
|---|---|---|
| Left-Left (LL) | Unbalanced node and its left child node are both left-heavy. | Single right rotation. |
| Right-Right (RR) | Unbalanced node and its right child node are both right-heavy. | Single left rotation. |
| Left-Right (LR) | Unbalanced node is left-heavy, and its left child node is right-heavy. | Left rotation on left child node, then right rotation on unbalanced node. |
| Right-Left (RL) | Unbalanced node is right-heavy, and its right child node is left-heavy. | Right rotation on right child node, then left rotation on unbalanced node. |

### Time Complexity

The time complexity for search, insert, and delete operations on an AVL Tree is O(log n), which is significantly faster than the O(n) time complexity for unbalanced Binary Search Trees. This is because the height of an AVL Tree is guaranteed to be logarithmic in the number of nodes, even in the worst case.

I hope this markdown file is helpful!
