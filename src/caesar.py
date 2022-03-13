# Program to encrypt and decrypt messages using a Caesar cipher

def main():
    message = input("Enter the message: ")
    key = int(input("Enter the key: "))
    if input("Do you want to encrypt or decrypt the message? (E/D): ") == "D":
        print("The decrypted message is:", caesar(message, key, False))
    else:
        print("The encrypted message is:", caesar(message, key))

# Apply Caesar cipher to message using key
def caesar(message, key, encrypt=True):
    encrypted_message = ""
    for ch in message:
        code = ord(ch) + key if encrypt else ord(ch) - key
        encrypted_message += chr(code)
    return encrypted_message

if __name__ == "__main__":
    main()
