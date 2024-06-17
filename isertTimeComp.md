# Insertion Sort Time Complexity

Insertion Sort sorts an array of `n` values.

On average, each value must be compared to about `n/2` other values to find out where to insert it.

And Insertion Sort must run the loop to insert a value in its correct place approximately `n` times.

We get the time complexity for Insertion Sort:

**O(n²)**

---

The time complexity for Insertion Sort can be displayed like this:

![Insertion Sort Time Complexity](https://www.bigocheatsheet.com/img/time-complexity-insertion-sort.png)

## Simulation of Insertion Sort

Use the simulation below to see how the theoretical time complexity **O(n²)** compares to the actual number of operations performed by the Insertion Sort algorithm.

### Code

```python
import matplotlib.pyplot as plt
import random
import time

def insertion_sort(arr):
    comparison_count = 0
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            comparison_count += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if j >= 0:  # Increment comparison count for the final comparison where the while loop condition fails
            comparison_count += 1
    return comparison_count

def simulate_insertion_sort(array_size):
    array = [random.randint(0, 1000) for _ in range(array_size)]
    start_time = time.time()
    comparison_count = insertion_sort(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return array_size, comparison_count, elapsed_time

sizes = [10, 50, 100, 200, 500]
results = [simulate_insertion_sort(size) for size in sizes]

# Plot the results
sizes, comparisons, times = zip(*results)
plt.figure(figsize=(10, 5))
plt.plot(sizes, [size**2 for size in sizes], 'r--', label="O(n²)")
plt.scatter(sizes, comparisons, color='blue', label="Insertion Sort Comparisons")
plt.xlabel("Array Size")
plt.ylabel("Number of Comparisons")
plt.title("Insertion Sort Time Complexity")
plt.legend()
plt.show()
