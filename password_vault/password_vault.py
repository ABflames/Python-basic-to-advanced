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

password = generate_password(length) #calling it outside of the function..
encrypted_password = encrypt(password)
decrypted_password = decrypt(encrypted_password)

print("Generated password:", password)
print("Encrypted password:", encrypted_password)
print("Decrypted password:", decrypted_password)

with open("passwords.txt", "a") as file: #"a" -> append mode, so it doesn't overwrite existing passwords.
        #file.write(password + "\n") # /n to avoid overwriting.
    file.write(f"{service}: {encrypted_password}\n")
        

