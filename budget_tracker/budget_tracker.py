#expenses = {
#    "amount": 500,
#    "category": "Food",
#    "description": "Dinner"}

#print (expenses)

import csv

def load_expenses():
    expenses = []
    
    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
        
            for row in reader:
                amount = float(row["amount"]) # row is already a dictionary because we're using DictReader().
                category = row["category"]
                description = row["description"]
            
                expense = {  # individual dictionary 2
                        "amount": amount,
                        "category": category,
                        "description": description
                    }
                expenses.append(expense)
                
    except FileNotFoundError:
        print("No existing expenses file found. Starting fresh.")
            
    return expenses

#loaded_expenses = load_expenses()
#print(" ")
#print("loaded_expenses")

#expenses = [] # an exmpty list
expenses = load_expenses()

choice = "yes"
total = 0
category_totals = {} #another dictionary

while choice == "yes":

    try:
        amount = float(input("Enter the amount: "))

    except ValueError:
        print("Invalid amount!")
        continue
    
    if amount <= 0:
        print("Amount must be greater than zero.")
        continue

    #category = input("Enter the category: ")
    #description = input("Enter the description: ")
    
    # a user shouldn't leave either field empty!
    
    category = input("Enter the category: ").strip()
    description = input("Enter the description: ").strip()
    # .strip() removes leading and trailing spaces.

    if not category or not description:
        print("Category and description cannot be empty.")
        continue

    expense = {  # individual dictionary
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    #print (expenses)
    choice = input("Add another expense? (yes/no): ").lower().strip()
    
#print("All expenses: ", expenses)

print("\nYOUR EXPENSES")
print("-" * 60)
print(f"{'No.':<5}{'Category':<20}{'Description':<25}{'Amount':>15}")
print("-" * 60)

for index, expense in enumerate(expenses, start=1):
    #print(index, expense)
    #print(index, expense["category"], ":", expense["description"], ":", "₹", expense["amount"])
    print(f"{index:<5}{expense['category']:<20}{expense['description']:<25}{'₹' + format(expense['amount'], '.2f'):>15}")  #format() converts a value into a formatted string.

for expense in expenses:
    total = total + expense["amount"]
    category = expense["category"]
    amount = expense["amount"]
    
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

print("\nCATEGORY-WISE SPENDING")
print("-" * 40)

for category, amount in category_totals.items():
    print(f"{category:<20}₹{amount:>15.2f}")
       
#print("Total spending: ", total)
print("-" * 60)
print(f"{'Total Spending':<45}₹{total:>14.2f}")
#print("Category wise spending: ", category_totals)

with open("expenses.csv", "w", newline="") as file:
    writer = csv.writer(file) # creating a csv writer.
    
    writer.writerow(["amount", "category", "description"])
    
    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]
        description = expense["description"]
        
        writer.writerow([amount, category, description])
        
#def load_expenses():
#    expenses = []
#    
#    with open("expenses.csv", "r", newline="") as file:
#        reader = csv.DictReader(file)
#        
#        for row in reader:
#            amount = float(row["amount"]) # row is already a dictionary because we're using DictReader().
#            category = row["category"]
#            description = row["description"]
#            
#            expense = {  # individual dictionary 2
#                    "amount": amount,
#                    "category": category,
#                    "description": description
#                }
#            expenses.append(expense)
#            
#    return expenses
#
#loaded_expenses = load_expenses()
#print(" ")
#print("loaded_expenses")