# Selection Sort Time Complexity

Selection Sort sorts an array of `n` values.

On average, about `n²` elements are compared to find the lowest value in each loop.

And Selection Sort must run the loop to find the lowest value approximately `n` times.

We get the time complexity:

**O(n²)**

---

The time complexity for the Selection Sort algorithm can be displayed in a graph like this:

![Selection Sort Time Complexity](https://www.bigocheatsheet.com/img/time-complexity-selection-sort.png)

As you can see, the run time is the same as for Bubble Sort: The run time increases really fast when the size of the array is increased.

## Simulation of Selection Sort

You can simulate Selection Sort below, where the red dashed line represents the theoretical time complexity **O(n²)**. You can choose a number of values `n`, and run an actual Selection Sort implementation where the operations are counted and the count is marked as a blue cross in the plot below.

### Code

```python
import matplotlib.pyplot as plt
import random
import time

def selection_sort(arr):
    n = len(arr)
    comparison_count = 0
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            comparison_count += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return comparison_count

def simulate_selection_sort(array_size):
    array = [random.randint(0, 1000) for _ in range(array_size)]
    start_time = time.time()
    comparison_count = selection_sort(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return array_size, comparison_count, elapsed_time

sizes = [10, 50, 100, 200, 500]
results = [simulate_selection_sort(size) for size in sizes]

# Plot the results
sizes, comparisons, times = zip(*results)
plt.figure(figsize=(10, 5))
plt.plot(sizes, [size**2 for size in sizes], 'r--', label="O(n²)")
plt.scatter(sizes, comparisons, color='blue', label="Selection Sort Comparisons")
plt.xlabel("Array Size")
plt.ylabel("Number of Comparisons")
plt.title("Selection Sort Time Complexity")
plt.legend()
plt.show()
