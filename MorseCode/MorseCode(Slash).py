def morse_to_text(morse_code):
    # Define the Morse code dictionary
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': '\'',
        '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
        '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-',
        '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
    }

    # Split the Morse code into words using '/' as a delimiter
    words = morse_code.split('/')
    decoded_message = []

    for word in words:
        # Split each word into individual Morse code symbols (separated by spaces)
        letters = word.split(' ')
        decoded_word = ''

        for letter in letters:
            # Translate each Morse code symbol to its corresponding letter
            decoded_word += morse_dict.get(letter, '')

        # Append the decoded word to the decoded message
        decoded_message.append(decoded_word)

    # Join the decoded words with spaces to form the final message
    return ' '.join(decoded_message)

# Input Morse code with words separated by '/'
morse_code = "... --- ... / -.-.-- / .... . .-.. .-.. --- / .-- --- .-. .-.. -.."

# Decode and print the result
decoded_message = morse_to_text(morse_code)
print(decoded_message)
