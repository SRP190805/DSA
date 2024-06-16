# Fibonacci Numbers: Loops vs Recursion

This document illustrates three different implementations to find Fibonacci numbers: using a for loop, using recursion to print the first 20 Fibonacci numbers, and using recursion to find the \( n \)th Fibonacci number.

## 1. Implementation Using a For Loop

To find the first 20 Fibonacci numbers using a for loop, the code needs to:
- Use two variables to hold the previous two Fibonacci numbers.
- Use a for loop to run 18 times.
- Create new Fibonacci numbers by adding the two previous ones.
- Print the new Fibonacci number.
- Update the variables that hold the previous two Fibonacci numbers.

### Code

```python
def fibonacci_for_loop(n):
    a, b = 0, 1
    print(a, b, end=' ')
    for _ in range(n-2):
        next_fib = a + b
        print(next_fib, end=' ')
        a, b = b, next_fib

# Example usage to print the first 20 Fibonacci numbers
fibonacci_for_loop(20)
