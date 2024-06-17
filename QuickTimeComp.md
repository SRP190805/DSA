# Quicksort Time Complexity

The worst case scenario for Quicksort is **O(n²)**. This is when the pivot element is either the highest or lowest value in every sub-array, which leads to a lot of recursive calls. With our implementation above, this happens when the array is already sorted.

But on average, the time complexity for Quicksort is actually just **O(n log n)**, which is a lot better than for the previous sorting algorithms we have looked at. That is why Quicksort is so popular.

## Time Complexity Comparison

Below you can see the significant improvement in time complexity for Quicksort in an average scenario **O(n log n)**, compared to the previous sorting algorithms Bubble Sort, Selection Sort, and Insertion Sort with time complexity **O(n²)**:

### Time Complexity Graph

![Time Complexity Comparison](https://www.bigocheatsheet.com/img/time-complexity-quicksort.png)

### Explanation

The recursion part of the Quicksort algorithm is actually a reason why the average sorting scenario is so fast. For good picks of the pivot element, the array will be split in half somewhat evenly each time the algorithm calls itself. So the number of recursive calls does not double, even if the number of values `n` doubles.

### Summary of Time Complexities

- **Best Case**: **O(n log n)** - Occurs when the pivot element always splits the array into two equal halves.
- **Average Case**: **O(n log n)** - Occurs when the pivot element splits the array into two nearly equal halves.
- **Worst Case**: **O(n²)** - Occurs when the pivot element is always the smallest or largest element in the array (e.g., when the array is already sorted).

### Comparison with Other Sorting Algorithms

- **Bubble Sort**: **O(n²)**
- **Selection Sort**: **O(n²)**
- **Insertion Sort**: **O(n²)**
- **Quicksort**: **O(n log n)** (Average and Best Case)

## Simulation of Quicksort Time Complexity

To simulate the time complexity of Quicksort, you can use the following Python code:

### Code

```python
import matplotlib.pyplot as plt
import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def simulate_quicksort(array_size):
    array = [random.randint(0, 1000) for _ in range(array_size)]
    start_time = time.time()
    quicksort(array, 0, len(array) - 1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return array_size, elapsed_time

sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000]
results = [simulate_quicksort(size) for size in sizes]

# Plot the results
sizes, times = zip(*results)
plt.figure(figsize=(10, 5))
plt.plot(sizes, [size * math.log(size) for size in sizes], 'r--', label="O(n log n)")
plt.scatter(sizes, times, color='blue', label="Quicksort Time")
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.title("Quicksort Time Complexity")
plt.legend()
plt.show()
