# Binary Search Time Complexity

Binary Search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search interval in half.

## Time Complexity

The time complexity for Binary Search is **O(log₂ n)**.

### Explanation

- **Best Case**: If the target value is found at the middle of the array, only one comparison is needed, resulting in **O(1)** time complexity.
  
- **Worst Case**: If the target value is not found in the array, Binary Search performs **O(log₂ n)** comparisons.
  
- **Average Case**: Binary Search consistently operates with **O(log₂ n)** time complexity due to its halving of the search interval at each step.

### Note

The base of the logarithm in the time complexity notation **O(log₂ n)** emphasizes that the search area is halved in each step of the algorithm, which is fundamental to Binary Search.

### Visualization

The plot below illustrates the time complexity for Binary Search:

![Time Complexity for Binary Search](https://www.bigocheatsheet.com/img/time-complexity-binary-search.png)

### Simulation

You can simulate Binary Search for different numbers of elements in a sorted array to observe how the number of comparisons scales with the size of the array. Try searching for different values in the sorted array to see how efficiently Binary Search operates.

