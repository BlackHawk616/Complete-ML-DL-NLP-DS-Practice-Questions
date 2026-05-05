"""Write programs using:

- `map()` to square numbers in a list
- `filter()` to extract even numbers from a list"""

def square_numbers(numbers):
    return list(map(lambda x: x**2, numbers))

def filter_evennumbers(numbers):
    return list(filter(lambda x: x % 2 ==0, numbers))

lis1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
squared = square_numbers(lis1)
even_numbers = filter_evennumbers(lis1)
print("Squared numbers:", squared)
print("Even numbers:", even_numbers)