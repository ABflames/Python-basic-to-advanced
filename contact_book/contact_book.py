import json

print("=" * 40)
print("TERMINAL CONTACT BOOK".center(40)) #.center(40) method is used to center the string within a specified width.
print("=" * 40)

print()

with open("contacts.json", "r") as file:
    contacts = json.load(file)

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

        contacts.append(contact) # takes dictionary and adds at the end of list
        #print(contacts)
        with open("contacts.json", "w") as file: # w -> write mode, if file doesn't exist it will create a new file
            json.dump(contacts, file) 
        
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
        search_name = input("Enter the name: ") 
        
        found = False
        
        for contact in contacts:
            if search_name == contact["name"]:
                found = True
                print(f"\nName : {contact['name']}") # usage of f-strings
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print("-" * 30)   
        
        if not found:
            print("\nNo contacts found.")
            
    elif choice == "4":
        update_name = input("Enter the name of the contact to update: ")
        
        found = False
        #entity_update = input("What do you want to update?: \n1. Name\n2. Phone\n3. Email\nEnter your choice: ")
        
        for contact in contacts:
            if update_name == contact["name"]:
                found = True
                print("\nContact found!")
                print(f"\nName : {contact['name']}") # usage of f-strings
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print("-" * 30) 
                
                entity_update = input("What do you want to update?: \n1. Name\n2. Phone\n3. Email\nEnter your choice: ")
                
                if entity_update == "1":
                    new_name = input("Enter the new name: ")
                    contact["name"] = new_name
                    print("\nContact updated successfully!")
                    
                elif entity_update == "2":
                    new_phone = input("Enter the new phone number: ")
                    contact["phone"] = new_phone
                    print("\nContact updated successfully!")
                    
                elif entity_update == "3":
                    new_email = input("Enter the new email: ")
                    contact["email"] = new_email
                    print("\nContact updated successfully!")
                    
                else:
                    print("Invalid choice. Please try again.")
                    
                with open("contacts.json", "w") as file:
                    json.dump(contacts, file)
                    
        if not found:
            print("\nContact not found.")
        
    elif choice == "5":
        remove_contact = input("Enter the contact you want to delete: ")
        
        found = False
        
        for contact in contacts:
            if remove_contact == contact["name"]:
                found = True
                print("\nContact found!")
                print(f"\nName : {contact['name']}") # usage of f-strings
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print("-" * 30) 
                
                confirmation = input("Are you sure you want to delete this contact? (y/n): ")
                
                if confirmation == "y":
                    contacts.remove(contact)
                    with open("contacts.json", "w") as file:
                        json.dump(contacts, file)
                        
                    print("\nContact deleted successfully!")
                    
                else:
                    print("\nContact not removed!")
                    
        if not found:
            print("\nContact not found.")
                    
    elif choice == "6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
        
        
