import secrets

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

#password = secrets.choice(characters)
#password = ""

#for i in range(8):
#    password += secrets.choice(characters)
    
def generate_password(length):
    password = ""

    for i in range(length):
        password += secrets.choice(characters) # Generate a random character/string from the characters string

    return password

def encrypt(text):
    encrypted = ""
    
    for char in text:
        position = characters.index(char)
        new_position = (position + 2) % len(characters) # % -> for loop
        encrypted_char = characters[new_position]
        encrypted += encrypted_char
        
    return encrypted

def decrypt(text):
    decrypted = ""
    
    for char in text:
        position = characters.index(char)
        new_position = (position - 2) % len(characters)
        decrypted_char = characters[new_position]
        decrypted += decrypted_char
    
    return decrypted

def load_vault():
    try:
        with open("passwords.txt", "r") as file:
                data = file.read()
                
        return data
        
    except FileNotFoundError:
        return ""

def add_password():
    service = input("Enter the service name: ").strip() #.strip() removes any leading or trailing whitespace from the input string. THIS IS USED HERE JUST FOR LEARNING PURPOSE.

    if not service: #here .strip() is put to use.
        print("Service name cannot be empty.")
        return

    valid_length = False

    try:
        length = int(input("Enter password length: "))

        if length > 0:
            valid_length = True
        else:
            print("Password length must be greater than 0.")

    except ValueError:
        print("Please enter a valid number.")

    if valid_length:
        password = generate_password(length)
        encrypted_password = encrypt(password)

        print("Generated password:", password)
        print("Encrypted password:", encrypted_password)

        with open("passwords.txt", "a") as file:
            file.write(f"{service}: {encrypted_password}\n")

def view_passwords():
    vault_data = load_vault()
    entries = vault_data.splitlines()

    found = False

    for entry in entries:
        if ": " not in entry:
            print(f"Invalid vault entry skipped: {entry}")
            continue

        service, encrypted_password = entry.split(": ", 1)
        password = decrypt(encrypted_password)

        print(f"Service: {service}")
        print(f"Password: {password}")
        print("-" * 30)
        
        found = True
        
    if not found:
        print("No passwords found in the vault.")    
        
        
while True:
    print("\n===== PASSWORD VAULT =====")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        print("Exiting password vault...")
        break

    else:
        print("Invalid choice. Please try again.")