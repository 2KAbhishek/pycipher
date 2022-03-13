# Program to encrypt and decrypt messages using a Caesar cipher
def main():
    message = input("Enter the message: ")
    key = input("Enter the key: ")

    if input("Do you want to encrypt or decrypt the message? (E/D): ") == "D":
        print("The decrypted message is:", decrypt(message, key))
    else:
        print("The encrypted message is:", encrypt(message, key))

# Remove spaces from the message
def remove_spaces(message):
    return("".join(message.split()))

# Get back original message
def add_spaces(processed, original):
    processed = list(processed)
    for i in range(len(original)):
        if original[i] == ' ':
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
    stripped_message = remove_spaces(message)
    gen_key = generate_key(stripped_message, key)
    encrypted_message = []
    for i in range(len(stripped_message)):
        code = (ord(stripped_message[i]) + ord(gen_key[i])) % 26
        code += ord('A')
        encrypted_message.append(chr(code))
    return add_spaces("" . join(encrypted_message), message)

# Decrypt the message using the key
def decrypt(message, key):
    message = remove_spaces(message)
    key = generate_key(message, key)
    decypted_message = []
    for i in range(len(message)):
        x = (ord(message[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        decypted_message.append(chr(x))
    return("" . join(decypted_message))


if __name__ == "__main__":
    main()
