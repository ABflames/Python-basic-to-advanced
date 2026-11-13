#expenses = {
#    "amount": 500,
#    "category": "Food",
#    "description": "Dinner"}

#print (expenses)

expenses = [] # an exmpty list

choice = "yes"
#total = 0
category_totals = {} #another dictionary

while choice == "yes":

    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    description = input("Enter the description: ")

    expense = {  # individual dictionary
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    #print (expenses)
    choice = input("Add another expense? (yes/no): ")
    
#print("All expenses: ", expenses)

print("\nYOUR EXPENSES")

for index, expense in enumerate(expenses, start=1):
    #print(index, expense)
    #print(index, expense["category"], ":", expense["description"], ":", "₹", expense["amount"])
    print(f"{index}. {expense['category']} : {expense['description']} : ₹{expense['amount']:.2f}")

for expense in expenses:
    #total = total + expense["amount"]
    category = expense["category"]
    amount = expense["amount"]
    
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount
    
#print("Total spending: ", total)
print("Category wise spending: ", category_totals)






