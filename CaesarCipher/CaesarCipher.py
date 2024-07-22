def caesar_cipher_encrypt(plaintext, shift):

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

    return caesar_cipher_encrypt(ciphertext, -shift)

# Example usage:
ciphertext = "xqkwKBN{z0bib1wv_l3kzgxb3l_949in1i1}"

# Try all possible shifts from 1 to 26
for shift in range(1, 27):
    decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {decrypted_text}")
