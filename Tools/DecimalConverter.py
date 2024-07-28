def decimal_to_binary(decimal_number):
    # Convert decimal to binary
    binary_value = bin(decimal_number)
    return binary_value[2:]  # Remove the '0b' prefix

def decimal_to_octal(decimal_number):
    # Convert decimal to octal
    octal_value = oct(decimal_number)
    return octal_value[2:]  # Remove the '0o' prefix

def decimal_to_hexadecimal(decimal_number):
    # Convert decimal to hexadecimal
    hex_value = hex(decimal_number)
    return hex_value[2:]  # Remove the '0x' prefix

# Example usage
decimal_number = 100

binary_result = decimal_to_binary(decimal_number)
octal_result = decimal_to_octal(decimal_number)
hexadecimal_result = decimal_to_hexadecimal(decimal_number)

print("Decimal:", decimal_number)
print("Binary:", binary_result)
print("Octal:", octal_result)
print("Hexadecimal:", hexadecimal_result)
