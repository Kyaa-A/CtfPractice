def octal_to_binary(octal_string):
    # Convert octal string to decimal, then to binary
    decimal_value = int(octal_string, 8)
    binary_value = bin(decimal_value)
    return binary_value[2:]  # Remove the '0b' prefix

def octal_to_decimal(octal_string):
    # Convert octal string to decimal
    decimal_value = int(octal_string, 8)
    return decimal_value

def octal_to_hexadecimal(octal_string):
    # Convert octal string to decimal, then to hexadecimal
    decimal_value = int(octal_string, 8)
    hex_value = hex(decimal_value)
    return hex_value[2:]  # Remove the '0x' prefix

# Example usage
octal_string = "144"  # This is 100 in octal

binary_result = octal_to_binary(octal_string)
decimal_result = octal_to_decimal(octal_string)
hexadecimal_result = octal_to_hexadecimal(octal_string)

print("Octal:", octal_string)
print("Binary:", binary_result)
print("Decimal:", decimal_result)
print("Hexadecimal:", hexadecimal_result)
