# Stacks

A stack is a data structure that can hold many elements.

Think of a stack like a pile of pancakes.

In a pile of pancakes, the pancakes are both added and removed from the top. So when removing a pancake, it will always be the last pancake you added. This way of organizing elements is called LIFO: Last In First Out.

## Basic Operations

Basic operations we can do on a stack are:

- **Push**: Adds a new element on the stack.
- **Pop**: Removes and returns the top element from the stack.
- **Peek**: Returns the top element on the stack.
- **isEmpty**: Checks if the stack is empty.
- **Size**: Finds the number of elements in the stack.

## Applications of Stacks

Stacks can be used to:

- Implement undo mechanisms.
- Revert to previous states.
- Create algorithms for depth-first search in graphs.
- Implement backtracking.

## Stack Implementation using Arrays

Stacks can be implemented by using arrays or linked lists.

### Benefits of Using Arrays for Stacks

- **Memory Efficient**: Array elements do not hold the next element's address like linked list nodes do.
- **Easier to Implement and Understand**: Using arrays to implement stacks require less code than using linked lists, and for this reason, it is typically easier to understand as well.

### Downsides of Using Arrays for Stacks

- **Fixed Size**: An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements.

### Stack Visualization

This is how it looks like when we use an array as a stack:

