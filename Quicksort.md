# Quicksort

As the name suggests, Quicksort is one of the fastest sorting algorithms.

The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that lower values are on the left of the pivot element, and higher values are on the right of it.

In this tutorial, the last element of the array is chosen to be the pivot element, but we could also have chosen the first element of the array, or any element in the array really.

Then, the Quicksort algorithm does the same operation recursively on the sub-arrays to the left and right side of the pivot element. This continues until the array is sorted.

## How Quicksort Works

1. **Choose a Pivot**: Choose a pivot element from the array.
2. **Partition the Array**: Rearrange the array so that all elements less than the pivot are on the left, and all elements greater than the pivot are on the right.
3. **Recursively Apply**: Recursively apply the above steps to the sub-array of elements with smaller values and the sub-array of elements with greater values.

## Example: Quicksort in Python

### Code

```python
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

# Example usage
example_array = [10, 7, 8, 9, 1, 5]
print("Original array:", example_array)
quicksort(example_array, 0, len(example_array) - 1)
print("Sorted array:", example_array)
