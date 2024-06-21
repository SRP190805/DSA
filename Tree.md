## Trees: A Hierarchical Data Structure

Unlike linear data structures like arrays or linked lists, Trees are hierarchical, allowing for branching and non-linear organization of data. Similar to linked lists, each node in a tree contains data and references to other nodes. 

### Tree Applications

Trees find application in various scenarios:

* **Hierarchical Data:** Representing file systems, organizational charts, and other inherently hierarchical structures.
* **Databases:** Facilitating efficient data retrieval.
* **Routing Tables:** Used for routing data packets in network algorithms.
* **Sorting and Searching:** Employed for sorting and searching data efficiently.
* **Priority Queues:** Priority queues, such as binary heaps, often utilize tree structures.

### Tree Terminology

* **Root Node:** The initial node at the top of the tree hierarchy.
* **Edge:** A connection between two nodes.
* **Parent Node:** A node with links to child nodes. Also called an internal node.
* **Child Node:** A node linked from a parent node. Can have zero, one, or many children.
* **Leaf Node (Leaf):** A node without any child nodes.
* **Tree Height:** The maximum number of edges from the root to a leaf node.
* **Node Height:** The maximum number of edges between a specific node and a leaf node.
* **Tree Size:** The total number of nodes in the tree.

### Types of Trees

Trees are a cornerstone of computer science, especially for representing hierarchical relationships. Here's an overview of some important tree types:

* **Binary Trees:** Each node can have a maximum of two children, a left child and a right child. They serve as the foundation for more complex trees like binary search trees and AVL trees.
* **Binary Search Trees (BSTs):** A specific type of binary tree where each node has a value greater than all its left children and less than all its right children. This structure enables efficient searching.
* **AVL Trees:** A self-balancing binary search tree. For every node, the height difference between the left and right subtrees is at most one. Rotations are performed during insertions and deletions to maintain this balance, ensuring efficient operations.

These tree types, along with animations and implementation details, will be covered in separate sections for a deeper understanding.
