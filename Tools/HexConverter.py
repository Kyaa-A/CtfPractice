def hexadecimal_to_binary(hex_string):
    # Convert hexadecimal string to decimal, then to binary
    decimal_value = int(hex_string, 16)
    binary_value = bin(decimal_value)
    return binary_value[2:]  # Remove the '0b' prefix

def hexadecimal_to_octal(hex_string):
    # Convert hexadecimal string to decimal, then to octal
    decimal_value = int(hex_string, 16)
    octal_value = oct(decimal_value)
    return octal_value[2:]  # Remove the '0o' prefix

def hexadecimal_to_decimal(hex_string):
    # Convert hexadecimal string to decimal
    decimal_value = int(hex_string, 16)
    return decimal_value

# Example usage
hex_string = "64"  # This is 100 in hexadecimal

binary_result = hexadecimal_to_binary(hex_string)
octal_result = hexadecimal_to_octal(hex_string)
decimal_result = hexadecimal_to_decimal(hex_string)

print("Hexadecimal:", hex_string)
print("Binary:", binary_result)
print("Octal:", octal_result)
print("Decimal:", decimal_result)
