# Program to encrypt and decrypt messages using a Caesar cipher

def main():
    message = input("Enter the message: ")
    key = int(input("Enter the key: "))
    if input("Do you want to encrypt or decrypt the message? (E/D): ") == "D":
        decrypted_message = decrypt(message, key)
        print("The decrypted message is:", decrypted_message)
    else:
        encrypted_message = encrypt(message, key)
        print("The encrypted message is:", encrypted_message)

# Encrypt the message using the key
def encrypt(message, key):
    encrypted_message = ""
    for ch in message:
        encrypted_message += chr(ord(ch) + key)
    return encrypted_message

# Decrypt the message using the key
def decrypt(message, key):
    decrypted_message = ""
    for ch in message:
        decrypted_message -= chr(ord(ch) - key)
    return decrypted_message

if __name__ == "__main__":
    main()
