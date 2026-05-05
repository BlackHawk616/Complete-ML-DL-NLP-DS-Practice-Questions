# Write a program to flatten a nested list (of any depth) into a single list.

nestedlist = [[1,2,3,4,5,6,7],[12,3,5,515,61,6,[1,1,1],2,523,523,2,3,4,43,],]

def flatten(nestedlist):
    flattnelist = []
    for item in nestedlist:
        if type(item) == list:
            flattnelist.extend(flatten(item)) # Recursive Call to flatten the sublist
        else:
            flattnelist.append(item)
    return flattnelist
print(flatten(nestedlist))