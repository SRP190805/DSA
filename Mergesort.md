# Merge Sort

The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by recursively dividing it into halves, sorting those halves, and then merging them back together in sorted order.

## How Merge Sort Works

1. **Divide**: The algorithm starts by recursively dividing the array into smaller sub-arrays until each sub-array consists of only one element.

2. **Conquer**: After reaching the base case (single element sub-arrays), the algorithm starts merging these sub-arrays back together. During the merge process, it compares the smallest elements of each sub-array and puts them in order, resulting in a sorted array.

3. **Merge Operation**: The merge operation is the key part of Merge Sort. It involves merging two sorted arrays into a single sorted array.

## Example: Merge Sort in Python

### Code

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_half = arr[:mid]  # Dividing the elements into 2 halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
example_array = [12, 11, 13, 5, 6, 7]
print("Original array:", example_array)
merge_sort(example_array)
print("Sorted array:", example_array)
