import codecs

plaintext = "xqkwKBN{z0bib1wv_l3kzgxb3l_949in1i1}"
encoded_string = codecs.encode(plaintext, 'rot_13')
print("Encoded: " + encoded_string)
# 'sbbone'


# encoded_string = 'sbbone'
decoded_string = codecs.encode(encoded_string, 'rot_13')
print("Decoded: " + decoded_string)