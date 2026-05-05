# Create a program that takes two sets and performs union, intersection, difference, and symmetric difference.

def set_operations(set1, set2):
    union = set1.union(set2) # Union of two sets
    intersection = set1.intersection(set2) # Intersection of two sets
    difference = set1.difference(set2) # Difference of two sets
    symetric = set1.symmetric_difference(set2)

    return union, intersection, difference, symetric

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8} 
union, intersection, difference, symetric = set_operations(set1, set2)
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print("Symmetric Difference:", symetric)