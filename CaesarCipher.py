def caesar_cipher_encrypt(plaintext, shift):
    """
    Encrypts the plaintext using Caesar cipher with the given shift.
    
    :param plaintext: The plaintext message to encrypt (string).
    :param shift: The number of positions to shift each character (int).
    :return: The encrypted ciphertext (string).
    """
    ciphertext = []
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            ciphertext.append(chr(shifted))
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def caesar_cipher_decrypt(ciphertext, shift):
    """
    Decrypts the ciphertext encrypted with Caesar cipher using the given shift.
    
    :param ciphertext: The ciphertext message to decrypt (string).
    :param shift: The number of positions the characters were shifted (int).
    :return: The decrypted plaintext (string).
    """
    return caesar_cipher_encrypt(ciphertext, -shift)

# Example usage:
plaintext = "Hello"
shift = 3

encrypted_text = caesar_cipher_encrypt(plaintext, shift)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

print("Original:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
