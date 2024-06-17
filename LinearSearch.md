# Linear Search Algorithm

The Linear Search algorithm searches through an array sequentially to find a specified value and returns its index if found, otherwise it returns -1 indicating the value is not present.

## How Linear Search Works

1. **Initialization**: Start from the beginning of the array.

2. **Comparison**: Compare each element of the array with the target value sequentially.

3. **Finding the Value**: If the target value matches an element, return its index.

4. **Value Not Found**: If the entire array is traversed and the target value is not found, return -1.

## Example Implementation in Python

### Code

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
example_array = [12, 45, 23, 6, 8, 14, 39]
target_value = 14
index = linear_search(example_array, target_value)
if index != -1:
    print(f"Target value {target_value} found at index {index}.")
else:
    print(f"Target value {target_value} not found in the array.")
