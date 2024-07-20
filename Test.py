import codecs



# Encode 
print(codecs.encode(b"This_is_cool!",'base64'))

# Decode
print(codecs.decode(b"VGhpc19pc19jb29sIQ==\n",'base64'))  



























# print(codecs.encode(b"This_is_cool!",'hex'))