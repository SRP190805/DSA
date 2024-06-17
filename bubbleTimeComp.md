# Bubble Sort Time Complexity

For a general explanation of what time complexity is, visit [this page](https://en.wikipedia.org/wiki/Time_complexity).

For a more thorough and detailed explanation of Bubble Sort time complexity, visit [this page](https://en.wikipedia.org/wiki/Bubble_sort).

## Time Complexity of Bubble Sort

The Bubble Sort algorithm loops through every value in the array, comparing it to the value next to it. So for an array of `n` values, there must be `n` such comparisons in one loop.

And after one loop, the array is looped through again and again `n` times.

This means there are `n * n` comparisons done in total, so the time complexity for Bubble Sort is:

**O(n²)**

---

The graph describing the Bubble Sort time complexity looks like this:

![Bubble Sort Time Complexity](https://www.bigocheatsheet.com/img/time-complexity-bubble-sort.png)

As you can see, the run time increases really fast when the size of the array is increased.

Luckily, there are sorting algorithms that are faster than this, like Quicksort, that we will look at later.

## Simulation of Bubble Sort

You can simulate Bubble Sort below, where the red and dashed line is the theoretical time complexity O(n²). You can choose a number of values `n`, and run an actual Bubble Sort implementation where the operations are counted and the count is marked as a blue cross in the plot below.

### Code

```python
import matplotlib.pyplot as plt
import random
import time

def bubble_sort(arr):
    n
