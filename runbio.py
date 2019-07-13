#!/usr/bin/python3
import pandas as pd

# Open the Excel File
print("Open Excel File")
excel_file = 'data.xlsx'
data = pd.read_excel(excel_file)
print(data.head())

# Open the Output File
file = open("output.txt","a")

# Process the data
print("Finding Subset")
for x in range(data.shape[0]):
    dataA = data.iloc[x,0] #first column (A)
    dataB = data.iloc[x,5] #sixth column (F)

    # Data Validation
    if(pd.isna(dataA) or pd.isna(dataB)):
        continue # Skip NANs

    #Write Output Code
    output_text = '>' + str(dataA) + '\n' + str(dataB) + '\n'
    print(output_text)
    file.writelines(output_text)

# Save the Processed Data
print("Writing Output Data")
file.close()

# REFERENCES
# https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
# https://www.learnpython.org/en/Loops
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
