def binary_to_decimal(binary_string):
    # Convert binary string to decimal
    decimal_value = int(binary_string, 2)
    return decimal_value

def binary_to_octal(binary_string):
    # Convert binary string to decimal, then to octal
    decimal_value = int(binary_string, 2)
    octal_value = oct(decimal_value)
    return octal_value[2:]  # Remove the '0o' prefix

def binary_to_hexadecimal(binary_string):
    # Convert binary string to decimal, then to hexadecimal
    decimal_value = int(binary_string, 2)
    hex_value = hex(decimal_value)
    return hex_value[2:]  # Remove the '0x' prefix

# Example usage
binary_string = "1100"  # This is 100 in binary

decimal_result = binary_to_decimal(binary_string)
octal_result = binary_to_octal(binary_string)
hexadecimal_result = binary_to_hexadecimal(binary_string)

print("Binary:", binary_string)
print("Decimal:", decimal_result)
print("Octal:", octal_result)
print("Hexadecimal:", hexadecimal_result)
