# Linked Lists vs Arrays

## Linked Lists

A linked list is a linear data structure where each element is a separate object called a node. Each node contains data and a reference (link) to the next node in the sequence.

### Singly Linked List

In a singly linked list, each node points to the next node in the sequence:

![Singly Linked List](https://upload.wikimedia.org/wikipedia/commons/6/6d/Singly-linked-list.svg)

### Benefits of Linked Lists

- **Dynamic Size**: Nodes can be added or removed from a linked list without shifting other nodes.
- **Memory Allocation**: Nodes are stored in scattered memory locations, utilizing memory more flexibly compared to arrays.
- **Ease of Insertion/Deletion**: Adding or removing nodes involves changing references, rather than shifting elements like in arrays.

## Arrays

An array is a collection of elements stored in contiguous memory locations. Elements in an array are accessed using indices.

### Comparison with Linked Lists

- **Memory Usage**: Arrays require contiguous memory allocation, whereas linked lists use scattered memory.
- **Dynamic Size**: Arrays have fixed size after initialization, while linked lists can grow or shrink dynamically.
- **Access Time**: Accessing elements in arrays is faster (constant time complexity) compared to linked lists (linear time complexity for traversal).
- **Insertion/Deletion**: Inserting or deleting elements in arrays may require shifting elements, while linked lists only require adjusting pointers.

### Example Usage

#### Linked List Example in Python

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


