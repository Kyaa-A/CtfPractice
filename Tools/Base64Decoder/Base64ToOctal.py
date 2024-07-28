import base64

def base64_to_octal(base64_string):
    # Decode the Base64 string into bytes
    byte_data = base64.b64decode(base64_string)
    
    # Convert the bytes to an octal string with spaces between each value
    octal_string = ' '.join(format(byte, '03o') for byte in byte_data)
    
    return octal_string

# Example usage
base64_string = "SGVsbG8gV29ybGQh"  # This is "Hello World!" in Base64
octal_string = base64_to_octal(base64_string)
print("Octal string:", octal_string)
