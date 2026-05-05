# Write a program to read a JSON file, parse its contents, and display specific fields.

import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("The specified file was not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file format.")

def display_specific_fields(data, fields):
    with open('output.txt', 'w') as output_file:
        for field in fields:
            if field in data:
                output_file.write(f"{field}: {data[field]}\n")
            else:
                output_file.write(f"{field} not found in the JSON data.\n")

if __name__ == "__main__":
    json_data = read_json_file('PythonFoundations/test.json')
    if json_data:
        fields_to_display = ['name', 'age', 'city']
        display_specific_fields(json_data, fields_to_display)