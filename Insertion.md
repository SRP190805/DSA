# Insertion Sort

The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.

The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the entire array is sorted.

## How Insertion Sort Works

1. **Start with the First Element**: The first element of the array is considered sorted.
2. **Pick the Next Element**: Take the next element from the unsorted part of the array.
3. **Compare and Insert**: Compare the picked element with the elements in the sorted part of the array. Shift all the elements that are greater than the picked element to one position to the right. Insert the picked element at the correct position.
4. **Repeat**: Repeat steps 2 and 3 until the entire array is sorted.

## Example: Insertion Sort in Python

### Code

```python
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
example_array = [12, 11, 13, 5, 6]
print("Original array:", example_array)
insertion_sort(example_array)
print("Sorted array:", example_array)
