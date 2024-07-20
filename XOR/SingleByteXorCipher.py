# THIS IS FOR KEY = NUMBER

# def single_byte_xor_cipher(message, key):
#     return ''.join(chr(ord(char) ^ key) for char in message)

# message = "Hello"
# key = 42  
# encrypted = single_byte_xor_cipher(message, key)
# decrypted = single_byte_xor_cipher(encrypted, key)

# print("\nKey (Number): ")
# print("Original:", message)
# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)

# ==============================================================================

# THIS IS FOR KEY = LETTER

def single_byte_xor_cipher(message, key_char):
    # Convert the character key to its ASCII integer value
    key = ord(key_char)
    # Perform XOR operation on each character in the message with the key
    return ''.join(chr(ord(char) ^ key) for char in message)

# Example usage
message = "Hello"
key_char = 's'
encrypted = single_byte_xor_cipher(message, key_char)
decrypted = single_byte_xor_cipher(encrypted, key_char)

print("\nKey (Letter): ")
print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
