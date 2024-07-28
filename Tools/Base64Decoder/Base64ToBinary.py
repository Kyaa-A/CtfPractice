import base64

def base64_to_binary(base64_string):
    # Decode the Base64 string into bytes
    byte_data = base64.b64decode(base64_string)
    
    # Convert the bytes to a binary string with spaces between each value
    binary_string = ' '.join(format(byte, '08b') for byte in byte_data)
    
    return binary_string

# Example usage
base64_string = "SGVsbG8gV29ybGQh"  # This is "Hello World!" in Base64
binary_string = base64_to_binary(base64_string)
print("Binary string:", binary_string)
