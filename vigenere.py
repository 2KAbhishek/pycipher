# Program to encrypt and decrypt messages using a Caesar cipher
def main():
    message = input("Enter the message: ")
    stripped_message = "".join(message.split())

    key = input("Enter the key: ")
    gen_key = generate_key(stripped_message, key)

    if input("Do you want to encrypt or decrypt the message? (E/D): ") == "D":
        decrypted_message = decrypt(stripped_message, gen_key)
        print("The decrypted message is:", add_spaces(message, decrypted_message))
    else:
        encrypted_message = encrypt(stripped_message, gen_key)
        print("The encrypted message is:", add_spaces(message, encrypted_message))

# Get back original message
def add_spaces(message, processed):
    processed = list(processed)
    for i in range(len(message)):
        if message[i] == ' ':
            processed.insert(i, ' ')
    return ("" . join(processed))

# Generate the key with appropriate for cipher
def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return(key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

# Encrypt the message using the key
def encrypt(message, key):
    encrypted_message = []
    for i in range(len(message)):
        x = (ord(message[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypted_message.append(chr(x))
    return("" . join(encrypted_message))

# Decrypt the message using the key
def decrypt(message, key):
    decypted_message = []
    for i in range(len(message)):
        x = (ord(message[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        decypted_message.append(chr(x))
    return("" . join(decypted_message))


if __name__ == "__main__":
    main()
