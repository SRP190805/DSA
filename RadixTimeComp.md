# Radix Sort Time Complexity

Radix Sort sorts an array of `n` values based on the number of digits `k` in the highest value.

The time complexity for Radix Sort is:

O(n * k)

This means that Radix Sort depends both on the number of values `n` and the number of digits `k` in the highest value.

## Best Case Scenario

A best case scenario for Radix Sort occurs when there are many values to sort, but each value has a small number of digits. For example, if there are more than a million values to sort, and the highest value is 999 (just three digits), then the time complexity O(n * k) can be simplified to just O(n).

## Worst Case Scenario

A worst case scenario for Radix Sort would be if the number of digits `k` in the highest value is proportional to the number of values `n`. In this case, the time complexity would be O(n^2), which is not a common scenario but illustrates the upper bound.

## Average Case Scenario

The average or common case for Radix Sort is when the number of digits `k` is logarithmic relative to `n`, i.e., k(n) = log(n). In such a case, Radix Sort achieves a time complexity of O(n * log(n)). An example could be sorting 1,000,000 values where each value has 6 digits.

### Time Complexity Visualization

![Time Complexity for Radix Sort](https://www.bigocheatsheet.com/img/time-complexity-radix-sort.png)

The plot above illustrates the range of possible time complexities for Radix Sort. The red line represents the worst case scenario O(n^2), while the green line represents the best case scenario O(n).

### Simulations

You can simulate different scenarios of Radix Sort to observe how the number of operations varies between the worst case scenario (red line)
