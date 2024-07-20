# KEY MUST BE LETTER

def repeated_key_xor_cipher(message, key):
    key_length = len(key)
    return ''.join(
        chr(ord(char) ^ ord(key[i % key_length])) for i, char in enumerate(message)
    )

message = "Document" 
key = "abc"
encrypted = repeated_key_xor_cipher(message, key)
decrypted = repeated_key_xor_cipher(encrypted, key)

print("\nRepeated Key XOR Cipher:")
print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

# ===============================================================================================

# KEY MUST BE NUMBER

# def repeated_key_xor_cipher(message, key_number):
#     key = str(key_number)
#     key_length = len(key)

#     return ''.join(
#         chr(ord(char) ^ ord(key[i % key_length])) for i, char in enumerate(message)
#     )

# message = "Hello, World!"
# key_number = 123  
# encrypted = repeated_key_xor_cipher(message, key_number)
# decrypted = repeated_key_xor_cipher(encrypted, key_number)

# print("Repeated Key XOR Cipher:")
# print("Original:", message)
# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)
