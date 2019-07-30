#!/usr/bin/python3
import pandas as pd
import re

########################
### HELPER FUNCTIONS ###
########################

# This Function Counts Sequences
def count_sequence(sequence):
    countY = 0
    countW = 0
    countE = 0

    # Count Y
    matches = re.findall("(Y..P.(I|V|L))", sequence)
    #print(matches)
    countY += len(matches)
    #print(self.countY)

    # Count W
    matches = re.findall("(W..P.(I|V|L))", sequence)
    #print(matches)
    countW += len(matches)
    #print(self.countW)

    # Count E
    matches = re.findall("(E..P.(I|V|L))", sequence)
    #print(matches)
    countE += len(matches)
    #print(self.countE)

    return countY, countW, countE

####################
### MAIN ROUTINE ###
####################

# Open the Excel File
print("Opening Currated Dataset")
csv_file = '1-500-curated2.csv'
data = pd.read_csv(csv_file)
print(data.head())

# Desired Output:
# CSV file with 5 columns: QUERY, LEADER, NUM of Motif 1, NUM of Motif 2, NUM of Motif 3

# Open the Output File
print("Creating Output File")
file = open("output.csv","a")
file.writelines("Query,Leader,Number of Motif Y,Number of Motif W, Number of Motif E,Total Number of Motif Occurances\n")

# Process the data
print("Finding Subset")
for x in range(data.shape[0]):
    Query = data.iloc[x,0] #first column
    Leader = data.iloc[x,3] #thrid column

    # Count Occurances
    numY, numW, numE = count_sequence(Leader)
    numTot = numY + numW + numE

    # Create Output Line
    output_text = str(Query) + ',' + str(Leader) + ',' + str(numY) + ',' + str(numW) + ',' + str(numE) + ',' + str(numTot) + '\n'
    print(output_text)
    file.writelines(output_text)

# Save the Processed Data
print("Writing Output Data")
file.close()

# REFERENCES
# https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
# https://www.learnpython.org/en/Loops
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
