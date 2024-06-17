# Binary Search Algorithm

Binary Search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search interval in half.

## How Binary Search Works

1. **Initialization**: Start with the entire sorted array.

2. **Middle Element**: Calculate the middle index of the current array segment.

3. **Comparison**: Compare the target value with the middle element:
   - If they are equal, return the index of the middle element.
   - If the target value is less than the middle element, search the left half of the array.
   - If the target value is greater than the middle element, search the right half of the array.

4. **Repeat**: Continue the process until the target value is found or the search interval is empty.

5. **Value Not Found**: If the target value is not found after the entire array is searched, return -1.

## Example Implementation in Python

### Code

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate mid point
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Target value not found

# Example usage
sorted_array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_value = 12
index = binary_search(sorted_array, target_value)
if index != -1:
    print(f"Target value {target_value} found at index {index}.")
else:
    print(f"Target value {target_value} not found in the array.")
