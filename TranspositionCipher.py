def encrypt_message(message, key):
    # Determine the number of columns
    num_columns = len(key)
    
    # Create an array to store each column's content
    columns = ['' for _ in range(num_columns)]

    # Fill the columns with characters from the message
    for i, char in enumerate(message):
        column = i % num_columns
        columns[column] += char

    # Reorder columns based on the key
    # The key is a permutation of column indices
    ordered_columns = ['' for _ in range(num_columns)]
    for i, k in enumerate(key):
        ordered_columns[i] = columns[k]

    # Join the columns to get the encrypted message
    encrypted_message = ''.join(ordered_columns)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    # Determine the number of columns
    num_columns = len(key)

    # Calculate the number of full rows
    num_full_rows = len(encrypted_message) // num_columns

    # Calculate number of columns in the last row
    num_extra_columns = len(encrypted_message) % num_columns

    # Create an array to store each column's content
    columns = ['' for _ in range(num_columns)]

    # Distribute the encrypted message across the columns
    current_index = 0
    for i in range(num_columns):
        # Determine the number of characters in the column
        num_chars = num_full_rows + (1 if key.index(i) < num_extra_columns else 0)
        columns[i] = encrypted_message[current_index:current_index + num_chars]
        current_index += num_chars

    # Create the decrypted message by reading characters row by row
    decrypted_message = ''
    for row in range(num_full_rows + 1):
        for i in range(num_columns):
            if row < len(columns[i]):
                decrypted_message += columns[i][row]

    return decrypted_message

# Example usage
message = "This is a secret message"
key = [3, 1, 4, 2, 0]  # The order of columns

encrypted = encrypt_message(message, key)
print("Encrypted:", encrypted)

decrypted = decrypt_message(encrypted, key)
print("Decrypted:", decrypted)
