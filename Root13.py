import codecs

encoded_string = codecs.encode('Middle', 'rot_13')
print("Encoded: " + encoded_string)
# 'sbbone'


# encoded_string = 'sbbone'
decoded_string = codecs.encode(encoded_string, 'rot_13')
print("Decoded: " + decoded_string)