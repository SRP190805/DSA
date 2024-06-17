# Bubble Sort

Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

Run the simulation to see how it looks when the Bubble Sort algorithm sorts an array of values. Each value in the array is represented by a column.

The word 'Bubble' comes from how this algorithm works; it makes the highest values 'bubble up'.

## How Bubble Sort Works

1. **Compare Adjacent Elements**: Starting from the beginning of the array, compare each pair of adjacent elements.
2. **Swap if Necessary**: If the first element of the pair is greater than the second element, swap them.
3. **Repeat**: Move to the next pair and repeat the process until the end of the array. After each pass through the array, the highest value will have bubbled up to its correct position.
4. **Continue for All Elements**: Repeat the entire process for all elements until the array is sorted.

## Example: Bubble Sort in Python

### Code

```python
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Flag to detect any swap
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break

# Example usage
example_array = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", example_array)
bubble_sort(example_array)
print("Sorted array:", example_array)
