# Write a program that counts the frequency of each character in a given string and stores the result in a dictionary.

def count_characters(input_String):
    character_count = {} # Creating a dict to store the count of each character
    for char in input_String: # Tracversing each character in the input string
        if char in character_count: # If the character is already in the dictionary, increment its count
            character_count[char] += 1
        else:
            character_count[char] = 1 # If the character is not in the dictionary, add it with a count of 1
    return character_count

input_string = "hello world"

result = count_characters(input_string)

print(result)