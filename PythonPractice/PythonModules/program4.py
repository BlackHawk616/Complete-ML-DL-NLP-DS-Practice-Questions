# Creating a dataframe from list, dictionary and CSV file

import pandas as pd

# Creating a dataframe from list
data_list = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
df_list = pd.DataFrame(data_list, columns=['Name', 'Age'])

# Createing a dataframe from Dictonary
data_dict = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df_dict = pd.DataFrame(data_dict)

# Creating a dataframe from CSV File
# Assuming we have a CSV file named 'data.csv' with columns 'Name' and 'Age'
df_csv = pd.read_csv('data.csv')