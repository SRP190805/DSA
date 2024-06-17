# Merge Sort Time Complexity

Merge Sort is a divide-and-conquer algorithm that sorts an array by recursively dividing it into halves until each sub-array has only one element, and then merging those sub-arrays back together in sorted order.

## Time Complexity

The time complexity for Merge Sort is **O(n log n)**.

### Explanation

- **Best Case**: **O(n log n)** - Even if the array is already sorted, Merge Sort will still divide the array into halves and merge them, maintaining the same time complexity.
  
- **Average Case**: **O(n log n)** - Merge Sort consistently performs with this time complexity due to its divide-and-conquer approach.
  
- **Worst Case**: **O(n log n)** - In the worst case scenario, Merge Sort still operates in **O(n log n)** time, making it efficient across different datasets.

### Visualization

The plot below illustrates the time complexity for Merge Sort:

![Time Complexity for Merge Sort](https://www.bigocheatsheet.com/img/time-complexity-merge-sort.png)

### Simulation

You can simulate Merge Sort for different numbers of elements in an array to observe how the number of operations scales with the size of the array.

