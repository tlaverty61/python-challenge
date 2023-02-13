# establish base point 
import os
import csv

csvFilePath = os.path.join ("..", "Resources", "budget_data.csv")

with open(csvFilePath) as csvFile:

    csvReader = csv.reader(csvFile, delimiter=",")

    header = next(csvReader)

    print(header)
