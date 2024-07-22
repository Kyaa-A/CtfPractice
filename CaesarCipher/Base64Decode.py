import base64

def decode_base64(encoded_text):
    """
    Decodes a Base64 encoded string.

    :param encoded_text: The Base64 encoded string to decode (string).
    :return: The decoded string (string).
    """
    try:
        # Decode the Base64 encoded bytes
        decoded_bytes = base64.b64decode(encoded_text)
        
        # Convert bytes to string
        decoded_text = decoded_bytes.decode('utf-8')
        
        return decoded_text
    except Exception as e:
        return f"Error decoding Base64: {e}"

# Example usage
encoded_text = "xqkwKBN{z0bib1wv_l3kzgxb3l_949in1i1}"
decoded_text = decode_base64(encoded_text)

print("Encoded:", encoded_text)
print("Decoded:", decoded_text)
