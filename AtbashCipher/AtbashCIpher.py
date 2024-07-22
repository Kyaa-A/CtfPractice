def atbash_cipher(text):
    """
    Encodes or decodes the given text using the Atbash cipher.

    :param text: The text to encode or decode (string).
    :return: The encoded or decoded text (string).
    """
    # Define the Atbash transformation
    def atbash_transform(char):
        if char.isalpha():
            # Determine the base ASCII value for lowercase or uppercase
            base = ord('a') if char.islower() else ord('A')
            # Calculate the transformed character
            return chr(base + (25 - (ord(char) - base)))
        return char

    # Apply the transformation to each character in the text
    return ''.join(atbash_transform(char) for char in text)

# Example usage
plaintext = "krxlXGU{zgyzhs_xizxp_8z0uvwwx}"
ciphertext = atbash_cipher(plaintext)

print("Original:", plaintext)
print("Encoded/Decoded:", ciphertext)
