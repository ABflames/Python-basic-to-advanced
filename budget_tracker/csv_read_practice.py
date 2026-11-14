import csv

with open("expenses.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row)