import re

def identify_format(cipher_string):
    """Identify the format of the cipher string."""
    # Check if the string is hexadecimal
    if re.fullmatch(r'[0-9a-fA-F]+', cipher_string):
        return 'hex'
    # Check if the string is binary
    elif re.fullmatch(r'[01\s]+', cipher_string):
        return 'binary'
    # Check if the string is octal
    elif re.fullmatch(r'[0-7\s]+', cipher_string):
        return 'octal'
    # Check if the string is decimal
    elif re.fullmatch(r'[0-9\s]+', cipher_string):
        return 'decimal'
    else:
        return 'unknown'

def from_binary(binary_string):
    """Convert a binary string to bytes."""
    binary_string = binary_string.replace(' ', '')
    return int(binary_string, 2).to_bytes((len(binary_string) + 7) // 8, byteorder='big')

def from_octal(octal_string):
    """Convert an octal string to bytes."""
    octal_string = octal_string.replace(' ', '')
    return int(octal_string, 8).to_bytes((len(octal_string) + 2) // 3, byteorder='big')

def from_decimal(decimal_string):
    """Convert a decimal string to bytes."""
    decimal_string = decimal_string.replace(' ', '')
    return int(decimal_string, 10).to_bytes((len(decimal_string) + 2) // 3, byteorder='big')

def decode_and_find_flag(cipher_bytes):
    """Decode the cipher bytes and find the flag."""
    for i in range(0x00, 0xff):
        result = ''
        for j in cipher_bytes:
            result += chr(i ^ j)
        if 'actf{' in result:
            return result
    return None

# Input cipher string
cipher_string = 'fbf9eefce1f2f5eaffc5e3f5efc5efe9fffec5fbc5e9f9e8f3eaeee7'  # Change this for testing

# Identify format and decode accordingly
cipher_format = identify_format(cipher_string)

if cipher_format == 'hex':
    cipher_bytes = bytes.fromhex(cipher_string)
elif cipher_format == 'binary':
    cipher_bytes = from_binary(cipher_string)
elif cipher_format == 'octal':
    cipher_bytes = from_octal(cipher_string)
elif cipher_format == 'decimal':
    cipher_bytes = from_decimal(cipher_string)
else:
    print('Unknown format')
    cipher_bytes = None

# Decode and print the result if cipher_bytes is valid
if cipher_bytes:
    decoded_message = decode_and_find_flag(cipher_bytes)
    if decoded_message:
        print(f"Decoded from {cipher_format}: {decoded_message}")
    else:
        print("Flag not found.")
