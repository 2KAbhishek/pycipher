from .lib.util import *

# Program to encrypt and decrypt messages using vigenere cipher
def main():
    message = input("Enter the message: ")
    key = input("Enter the key: ")

    if input("Do you want to encrypt or decrypt the message? (E/D): ") == "D":
        print("The decrypted message is:", vigenere(message, key, False))
    else:
        print("The encrypted message is:", vigenere(message, key))

# Generate the key with appropriate for cipher
def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return(key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

# Apply vigener cipher to message using key
def vigenere(message, key, encrypt=True):
    stripped_message = remove_spaces(message)
    gen_key = generate_key(stripped_message, key)
    encrypted_message = []
    for i in range(len(stripped_message)):
        code = ord(stripped_message[i])
        code = (code + ord(gen_key[i])) % 26 if encrypt else (code - ord(gen_key[i])) % 26
        code += ord('A')
        encrypted_message.append(chr(code))
    return add_spaces("" . join(encrypted_message), message)

if __name__ == "__main__":
    main()
