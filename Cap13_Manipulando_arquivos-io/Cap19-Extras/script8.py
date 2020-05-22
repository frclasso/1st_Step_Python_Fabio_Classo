#!/usr/bin/env python3

import pandas as pd

# Assign spreadsheet filename: file
file = '../extras3_excel_files/battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())
print(df1.columns)
print()
# Load a sheet into a DataFrame by index: df2
df2 = xl.parse('2002')

# Print the head of the DataFrame df2
print(df2.head())
print(df2.columns)
