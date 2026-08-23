import secrets

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

#password = secrets.choice(characters)
#password = ""

#for i in range(8):
#    password += secrets.choice(characters)

valid_length = False

try:
    service = input("Enter the service name: ")
    length = int(input("Enter password length: "))
    
    if length > 0:
        valid_length = True
    else:
        print("Password length must be a positive integer(< 0).")        
except ValueError:
    print("Enter a valid number.")
    
if valid_length:
    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    print("Generated password:", password)
    
    with open("passwords.txt", "a") as file:
        #file.write(password + "\n") # /n to avoid overwriting.
        file.write(f"{service}: {password}\n")
        

