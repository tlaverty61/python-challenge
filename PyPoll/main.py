import os
import csv

results_csv = os.path.join("..", "Resources", "election_data.csv")

with open(results_csv) as csvFile:

        csvReader = csv.reader(csvFile, delimeter=",")
        header = next(csvReader)
        print(header)

