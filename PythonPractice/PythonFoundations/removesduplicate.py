# Write a Python program that takes a list of elements and returns a new list with all duplicate elements removed while preserving the original order.

def remove_duplicate(list1):
    newlist = []
    for i in list1:
        if i in newlist:
            continue
        else:
            newlist.append(i)
    
    return f"The list Is {newlist}"

duplicatelist = [12,12,41,15,16,15,6,23,2,6,7,3,1,70,7]
print(remove_duplicate(duplicatelist))
# 