# Hash Tables

Hash Tables are a powerful data structure designed for fast access, insertion, and deletion of elements. They excel in scenarios where frequent lookups, additions, and removals are necessary, even for large datasets.

# Why Hash Tables?

**Speed**: Compared to arrays or linked lists, Hash Tables offer significantly faster average-case performance for search, add, and delete operations.

**Direct Access**: Unlike linear search in arrays or linked lists, Hash Tables enable direct access to elements based on a calculated hash code.

# Core Concepts:

**Buckets**: The Hash Table is an array of buckets. Each element in the dataset is stored in a specific bucket.

**Hash Function**: A function that maps an element's value (key) to a unique number (hash code) used to determine the corresponding bucket. Ideally, a good hash function distributes elements evenly across buckets to minimize collisions.

**Collision**: When two elements have the same hash code, they collide and end up in the same bucket. Collision resolution techniques are needed to handle this.

# Operations:

## Search:

Calculate the hash code of the target element.
Access the bucket corresponding to that hash code.
Search within the bucket for the element (if collisions exist).
Return true if found, false otherwise.

## Add:

Calculate the hash code of the new element.
Access the bucket corresponding to that hash code.
If the bucket doesn't contain the element, add it.
Handle collisions (e.g., using chaining or separate chaining).

## Remove:

Calculate the hash code of the element to remove.
Access the bucket corresponding to that hash code.
Search for the element within the bucket.
If found, remove it.
Handle potential restructuring if the bucket becomes too empty.
