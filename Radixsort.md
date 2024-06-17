# Radix Sort

The Radix Sort algorithm sorts an array by individual digits, starting with the least significant digit (the rightmost one).

The radix (or base) is the number of unique digits in a number system. In the decimal system we normally use, there are 10 different digits from 0 to 9.

Radix Sort uses the radix so that decimal values are put into 10 different buckets (or containers) corresponding to the digit that is in focus, then put back into the array before moving on to the next digit.

Radix Sort is a non-comparative algorithm that only works with non-negative integers.

## How Radix Sort Works

1. **Initialize Buckets**: Create 10 buckets (one for each digit from 0 to 9).
2. **Sort by Each Digit**: Starting from the least significant digit (rightmost), place each number in the array into the corresponding bucket based on the current digit.
3. **Reassemble Array**: Collect the numbers from the buckets and reassemble the array.
4. **Repeat for Each Digit**: Move to the next more significant digit and repeat steps 2 and 3 until all digits have been processed.

## Example: Radix Sort in Python

### Code

```python
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count occurrences of digits
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy output array to arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Example usage
example_array = [355, 449, 442, 552, 586, 278, 534, 444, 462, 220]
print("Original array:", example_array)
radix_sort(example_array)
print("Sorted array:", example_array)
