cyphertext = 'rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7}' 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift_letter(letter, shift):
    global alphabet
    if letter.lower() in alphabet:
        if letter.isupper():
            index = alphabet.index(letter.lower())
            return alphabet[(index + shift) % 26].upper()
        else:
            index = alphabet.index(letter)
            return alphabet[(index + shift) % 26]

key = 'cylab'

def vigenere_decrypt(key,message):
    global alphabet
    solution =''
    key_index = 0
    key = key*100
    for letter in message:
        if letter.lower() in alphabet:
            key_letter = key[key_index]
            shift = alphabet.index(key_letter)
            key_index += 1
            print(shift, letter)
            solution += shift_letter(letter, -shift)
        else:
            solution += letter
    return solution

decrypted_message = vigenere_decrypt('cylab', cyphertext)      
print (decrypted_message) 

