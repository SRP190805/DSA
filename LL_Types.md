# Types of Linked Lists

There are three basic forms of linked lists:

1. Singly Linked Lists
2. Doubly Linked Lists
3. Circular Linked Lists

## Singly Linked Lists

A singly linked list is the simplest kind of linked list. It takes up less space in memory because each node has only one address to the next node, like in the image below.

![Singly linked list](images/singly_linked_list.png)

## Doubly Linked Lists

A doubly linked list has nodes with addresses to both the previous and the next node, like in the image below, and therefore takes up more memory. But doubly linked lists are good if you want to be able to move both up and down in the list.

![Doubly linked list](images/doubly_linked_list.png)

## Circular Linked Lists

A circular linked list is like a singly or doubly linked list with the first node, the "head", and the last node, the "tail", connected.

In singly or doubly linked lists, we can find the start and end of a list by just checking if the links are null. But for circular linked lists, more complex code is needed to explicitly check for start and end nodes in certain applications.

Circular linked lists are good for lists you need to cycle through continuously.

The image below is an example of a singly circular linked list:

![Circular singly linked list](images/circular_singly_linked_list.png)

The image below is an example of a doubly circular linked list:

![Circular doubly linked list](images/circular_doubly_linked_list.png)
