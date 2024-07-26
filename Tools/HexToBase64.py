import binascii
import base64

def hex_to_base64(hex_string):
    # Convert the hex string to bytes
    byte_data = binascii.unhexlify(hex_string)
    # Encode the byte data to a Base64 string
    base64_encoded = base64.b64encode(byte_data)
    # Decode the Base64 bytes to a string and return
    return base64_encoded.decode('utf-8')

# Input hexadecimal string
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# Convert and print the Base64 encoded result
base64_string = hex_to_base64(hex_string)
print(base64_string)
    