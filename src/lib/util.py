# Remove spaces from the message
def remove_spaces(message: str) -> str:
    return("".join(message.split()))

# Get back original message
def add_spaces(processed: str, original: str) -> str:
    processed = list(processed)
    for i in range(len(original)):
        if original[i] == ' ':
            processed.insert(i, ' ')
    return ("" . join(processed))
