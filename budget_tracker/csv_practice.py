import csv


with open("practice.csv", "w", newline="") as file: # newline=""	Prevents unwanted blank lines in CSV files on some systems.
    writer = csv.writer(file)                       # csv.writer(file)	Creates a CSV writer.

    writer.writerow(["amount", "category", "description"])
    writer.writerow([149.5, "Food", "Lunch"])