print("=" * 40)
print("TERMINAL CONTACT BOOK".center(40)) #.center(40) method is used to center the string within a specified width.
print("=" * 40)

print()

contacts = []

print("""1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit""")

while True:
    
    choice = input("Enter your choice : ")

    if choice == "1":
        name = input("Enter your name : ")
        phone = input("Enter your phone number : ")
        email = input("Enter your email : ")
        
        print("\nContact added successfully!")
        
        print()
        
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        #print(contacts)
        
    elif choice == "2":
       if not contacts:  # if contacts == []:
              print("\nNo contacts found.")
       else:
           for contact in contacts:
              # print("\nName:", contact["name"])
              # print("Phone:", contact["phone"])
              # print("Email:", contact["email"])
               print(f"\nName : {contact['name']}") # usage of f-strings
               print(f"Phone: {contact['phone']}")
               print(f"Email: {contact['email']}")
               print("-" * 30)
               
    elif choice == "3":
        print("\nSearch Contact:")
    elif choice == "4":
        print("\nUpdate Contact:")
    elif choice == "5":
        print("\nDelete Contact:")
    elif choice == "6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
    
