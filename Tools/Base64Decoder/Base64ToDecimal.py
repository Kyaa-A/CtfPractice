import base64

def base64_to_decimal(base64_string):
    # Decode the Base64 string into bytes
    byte_data = base64.b64decode(base64_string)
    
    # Convert the bytes to a decimal string with spaces between each value
    decimal_string = ' '.join(str(byte) for byte in byte_data)
    
    return decimal_string

# Example usage
base64_string = "SGVsbG8gV29ybGQh"  # This is "Hello World!" in Base64
decimal_string = base64_to_decimal(base64_string)
print("Decimal string:", decimal_string)
