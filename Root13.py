import codecs

plaintext = "Middle"
encoded_string = codecs.encode(plaintext, 'rot_13')
print("Encoded: " + encoded_string)
# 'sbbone'


# encoded_string = 'sbbone'
decoded_string = codecs.encode(encoded_string, 'rot_13')
print("Decoded: " + decoded_string)