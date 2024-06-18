# Variables, Arrays, and Linked Lists in Memory

## Variables in Memory

Let's imagine that we want to store the integer "17" in a variable `myNumber`. For simplicity, let's assume the integer is stored as two bytes (16 bits), and the address in memory to `myNumber` is `0x7F30`.

`0x7F30` is actually the address to the first of the two bytes of memory where the `myNumber` integer value is stored. When the computer goes to `0x7F30` to read an integer value, it knows that it must read both the first and the second byte, since integers are two bytes on this specific computer.

![Variable stored in memory](images/variable_in_memory.png)

The example above shows how an integer value is stored on the simple, but popular, Arduino Uno microcontroller. This microcontroller has an 8-bit architecture with a 16-bit address bus and uses two bytes for integers and two bytes for memory addresses. For comparison, personal computers and smartphones use 32 or 64 bits for integers and addresses, but the memory works basically in the same way.

## Arrays in Memory

To understand linked lists, it is useful to first know how arrays are stored in memory.

Elements in an array are stored contiguously in memory. That means that each element is stored right after the previous element.

The image below shows how an array of integers `myArray = [3, 5, 13, 2]` is stored in memory. We use a simple kind of memory here with two bytes for each integer, like in the previous example, just to get the idea.

![Array stored in memory](images/array_in_memory.png)

The computer has only got the address of the first byte of `myArray`, so to access the 3rd element with code `myArray[2]` the computer starts at `0x7F28` and jumps over the two first integers. The computer knows that an integer is stored in two bytes, so it jumps `2x2` bytes forward from `0x7F28` and reads value `13` starting at address `0x7F32`.

When removing or inserting elements in an array, every element that comes after must be either shifted up to make place for the new element, or shifted down to take the removed element's place. Such shifting operations are time-consuming and can cause problems in real-time systems for example.

The image below shows how elements are shifted when an array element is removed.

![Removing an element from an array](images/remove_element_from_array.png)

Manipulating arrays is also something you must think about if you are programming in C, where you have to explicitly move other elements when inserting or removing an element. In C this does not happen in the background.

In C you also need to make sure that you have allocated enough space for the array to start with, so that you can add more elements later.

## Linked Lists in Memory

Instead of storing a collection of data as an array, we can create a linked list.

Linked lists are used in many scenarios, like dynamic data storage, stack and queue implementation or graph representation, to mention some of them.

A linked list consists of nodes with some sort of data, and at least one pointer, or link, to other nodes.

A big benefit with using linked lists is that nodes are stored wherever there is free space in memory, the nodes do not have to be stored contiguously right after each other like elements are stored in arrays. Another nice thing with linked lists is that when adding or removing nodes, the rest of the nodes in the list do not have to be shifted.

The image below shows how a linked list can be stored in memory. The linked list has four nodes with values `3`, `5`, `13`, and `2`, and each node has a pointer to the next node in the list.

![Linked list nodes in memory](images/linked_list_in_memory.png)

Each node takes up four bytes. Two bytes are used to store an integer value, and two bytes are used to store the address to the next node in the list. As mentioned before, how many bytes that are needed to store integers and addresses depend on the architecture of the computer. This example, like the previous array example, fits with a simple 8-bit microcontroller architecture.

To make it easier to see how the nodes relate to each other, we will display nodes in a linked list in a simpler way, less related to their memory location, like in the image below:

![Linked list single node](images/linked_list_single_node.png)

If we put the same four nodes from the previous example together using this new visualization, it looks like this:

![Linked list example with addresses and values](images/linked_list_example.png)

As you can see, the first node in a linked list is called the "Head", and the last node is called the "Tail".

Unlike with arrays, the nodes in a linked list are not placed right after each other in memory. This means that when inserting or removing a node, shifting of other nodes is not necessary, so that is a good thing.

Something not so good with linked lists is that we cannot access a node directly like we can with an array by just writing `myArray[5]` for example. To get to node number 5 in a linked list, we must start with the first node called "head", use that node's pointer to get to the next node, and do so while keeping track of the number of nodes we have visited until we reach node number 5.

Learning about linked lists helps us to better understand concepts like memory allocation and pointers.

Linked lists are also important to understand before learning about more complex data structures such as trees and graphs, that can be implemented using linked lists.
