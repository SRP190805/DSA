# Queues

A queue is a data structure that can hold many elements.

Think of a queue as people standing in line in a supermarket.

The first person to stand in line is also the first who can pay and leave the supermarket. This way of organizing elements is called FIFO: First In First Out.

## Basic Operations
The basic operations we can perform on a queue are:

- **Enqueue**: Adds a new element to the queue.
- **Dequeue**: Removes and returns the first (front) element from the queue.
- **Peek**: Returns the first element in the queue.
- **isEmpty**: Checks if the queue is empty.
- **Size**: Finds the number of elements in the queue.

Experiment with these basic operations in the queue animation above.

## Implementation
Queues can be implemented using arrays or linked lists.

Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.

Queues are often mentioned together with Stacks, which is a similar data structure described on the previous page.

### Queue Implementation using Arrays
To better understand the benefits of using arrays or linked lists to implement queues, you should check out this page that explains how arrays and linked lists are stored in memory.

This is how it looks like when we use an array as a queue:

```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example Usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Outputs: 1
print(q.peek())     # Outputs: 2
print(q.is_empty()) # Outputs: False
print(q.size())     # Outputs: 1
