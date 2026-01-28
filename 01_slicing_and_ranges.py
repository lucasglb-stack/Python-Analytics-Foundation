"""
Topic: Python Slicing and Ranges
Purpose: Documentation of basic sequence manipulation for data analysis.
"""

# Section 1: Working with String Sequences (e.g., Operator/Employee IDs)
operators = ['Jon', 'Paul', 'Mary', 'Claire']

# Basic slicing follows the pattern [start:stop:step]
# Note: The stop index is always exclusive.
print(f"Mid-section subset (indices 1 to 2): {operators[1:3]}")

# Creating a shallow copy of the entire list
print(f"Full list copy: {operators[:]}")

# Slicing from a specific index to the end
print(f"From index 1 onwards: {operators[1:]}")

# Slicing from the start up to a specific index
print(f"First three elements: {operators[:3]}")


# Section 2: Numerical Sequences and Steps
# Common in time-series data or skipping rows in datasets
num_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using step to skip elements (Selecting even indices)
print(f"Every second element: {num_sequence[::2]}")

# The most idiomatic way to reverse a list in Python
print(f"Reversed sequence: {num_sequence[::-1]}")

# Selecting odd numbers (starting from index 1)
print(f"Every second element starting from index 1: {num_sequence[1::2]}")


# Section 3: The range() Function
# Essential for memory-efficient iterations and loop control

# range(stop) creates a range object from 0 to stop-1
range_obj = range(10)
print(f"Range object (lazy evaluation): {range_obj}")

# Converting range to list for visualization
list_from_range = list(range(10))
print(f"List generated from range: {list_from_range}")

# Specific range with (start, stop)
# Example: simulating a slice of IDs from 1 to 4
id_range = list(range(1, 5))
print(f"Generated range 1 to 4: {id_range}")

# Combining range with steps
# Efficiently generating a list of even numbers
even_range = list(range(0, 10, 2))
print(f"Even numbers using range step: {even_range}")
