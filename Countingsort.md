# Counting Sort

The Counting Sort algorithm sorts an array by counting the number of times each value occurs.

Counting Sort does not compare values like the previous sorting algorithms we have looked at, and only works on non-negative integers.

Furthermore, Counting Sort is fast when the range of possible values `k` is smaller than the number of values `n`.

## How Counting Sort Works

1. **Count Occurrences**: Create a count array to store the count of each unique value.
2. **Calculate Positions**: Modify the count array to store the cumulative sum of counts. This helps in placing the elements in the correct position in the output array.
3. **Build Output Array**: Construct the output array using the cumulative count array to place each element in its correct position.

## Example: Counting Sort in Python

### Code

```python
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)
    
    # Count occurrences
    for num in arr:
        count[num] += 1
    
    # Calculate cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output array
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

# Example usage
example_array = [4, 2, 2, 8, 3, 3, 1, 7, 7, 5, 6, 0, 9, 2, 1, 4, 7]
print("Original array:", example_array)
sorted_array = counting_sort(example_array)
print("Sorted array:", sorted_array)
