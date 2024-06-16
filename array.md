# Arrays

An array is a data structure used to store multiple elements. Arrays are used by many algorithms.

For example, an algorithm can be used to look through an array to find the lowest value, like the code below shows:

## Finding the Lowest Value in an Array

To find the lowest value in an array, we can use a simple algorithm that iterates through the array and keeps track of the smallest value found. Here's the Python implementation:

### Code

```python
def find_lowest_value(arr):
    # Initialize the minimum value with the first element of the array
    min_value = arr[0]
    
    # Loop through the array to find the minimum value
    for value in arr:
        if value < min_value:
            min_value = value
            
    return min_value

# Example usage
example_array = [34, 7, 23, 32, 5, 62]
lowest_value = find_lowest_value(example_array)
print(f"The lowest value in the array is: {lowest_value}")
