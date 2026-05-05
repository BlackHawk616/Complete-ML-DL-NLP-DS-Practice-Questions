"""
Write a program to sort a list of tuples based on:

- second element
- length of string  
    (using lambda functions)
"""

def sort_tuples(tuples_list):
    sorted_by_second = sorted(tuples_list, key=lambda x: x[1])
    sorted_by_length = sorted(tuples_list, key=lambda x: len(x[0]))
    return sorted_by_second, sorted_by_length

tuples_list = [("apple", 3), ("banana", 1), ("cherry", 2)]
sorted_by_second, sorted_by_length = sort_tuples(tuples_list)
print("Sorted by second element:", sorted_by_second)
print("Sorted by length of string:", sorted_by_length)