# Algorithm Time Complexity

## Run Time

When exploring algorithms, we often look at how long an algorithm takes to run relative to the size of the data set.

### Linear Time Complexity

In the example below, the time the algorithm needs to run is proportional, or linear, to the size of the data set. This is because the algorithm must visit every array element one time to find the lowest value. The loop must run `n` times, where `n` is the number of elements in the array.

For example, if the array has 5 values, the loop will run 5 times. If the array has 1000 values, the loop will run 1000 times.

### Example: Finding the Lowest Value in an Array

#### Code

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
