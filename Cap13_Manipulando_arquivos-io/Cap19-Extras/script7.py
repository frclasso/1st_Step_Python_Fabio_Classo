import pandas as pd

# Assign spreadsheet filename: file
file = '../extras3_excel_files/battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
