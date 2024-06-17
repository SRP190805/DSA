# Selection Sort

The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

The algorithm looks through the array again and again, moving the next lowest values to the front, until the array is sorted.

## How Selection Sort Works

1. **Find the Minimum Value**: Starting from the beginning of the array, find the smallest element in the array.
2. **Swap with the First Element**: Swap this smallest element with the first element of the array.
3. **Repeat for the Rest**: Repeat the process for the remaining part of the array (excluding the already sorted part).
4. **Continue Until Sorted**: Continue this process until the entire array is sorted.

## Example: Selection Sort in Python

### Code

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
example_array = [64, 25, 12, 22, 11]
print("Original array:", example_array)
selection_sort(example_array)
print("Sorted array:", example_array)
