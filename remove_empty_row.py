#This program reads in a .csv file called out.csv and removes all empty rows then creates a new file without the rows called FitBit.csv

import csv
with open('out.csv', 'r') as input1:
    output = open('FitBit.csv', 'w', newline='')
    writer = csv.writer(output)
    for row in csv.reader(input1):
        if any(row):
            writer.writerow(row)
output.close()
