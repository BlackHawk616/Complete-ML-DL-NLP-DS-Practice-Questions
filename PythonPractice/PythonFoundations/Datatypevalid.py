# Write a function that takes input and returns its data type (int, float, list, dict, etc.) and validates expected types.

def validate_data_type(value):
    if isinstance(value, int):
        return "The data type is int"
    elif isinstance(value, float):
        return "The Data type is float"
    elif isinstance(value, bool):
        return "The Data type is bool"
    elif isinstance(value, str):
        return "The Data type is str"
    elif isinstance(value, list):
        return "The Data type is list"
    elif isinstance(value, dict):
        return "The Data type is dict"
    else:
        return "Unknown data type"
    
# Takes the input from users and then validates

user_input = input("Enter a value: ")
result = validate_data_type(user_input)
print(result)   