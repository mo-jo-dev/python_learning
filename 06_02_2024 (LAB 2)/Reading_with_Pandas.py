import pandas as pd

file = pd.read_csv('salaries.csv')
print("The first five rows are: \n", file.head())
print("The last five rows are: \n", file.tail())
print("File information: \n", file.shape)