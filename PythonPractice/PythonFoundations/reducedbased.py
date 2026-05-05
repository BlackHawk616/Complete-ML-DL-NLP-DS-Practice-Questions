"""
Use `functools.reduce()` to:

- find the sum of a list
- find the product of elements""" 

from functools import reduce

def sum_list(numbers):
    return reduce(lambda x,y: x+y, numbers)

def product_list(numbers):
    return reduce(lambda x,y: x*y, numbers)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum_of_numbers = sum_list(numbers)
product_of_numbers = product_list(numbers)

print("Sum of numbers:", sum_of_numbers)
print("Product of numbers:", product_of_numbers)