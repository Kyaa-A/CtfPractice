import base64
import binascii

def base64_to_hex(base64_string):
    # Decode the Base64 string to bytes
    byte_data = base64.b64decode(base64_string)
    # Convert the byte data to a hexadecimal string
    hex_string = binascii.hexlify(byte_data)
    # Decode the hex bytes to a string and return
    return hex_string.decode('utf-8')

# Input Base64 string
base64_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

# Convert and print the hexadecimal result
hex_string = base64_to_hex(base64_string)
print(hex_string)
