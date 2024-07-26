def create_tap_code_grid():
    """Create a 5x5 grid for tap code, excluding 'K'."""
    alphabet = 'abcdefghijlmnopqrstuvwxyz'  # 'k' is omitted
    grid = {}
    index = 0
    for row in range(1, 6):
        for col in range(1, 6):
            if index < len(alphabet):
                grid[alphabet[index]] = (row, col)
                index += 1
    return grid

def decode_tap_code(tap_code_message):
    """Decode a tap code message."""
    grid = create_tap_code_grid()
    reverse_grid = {v: k for k, v in grid.items()}
    decoded_message = []

    # Split the encoded message by spaces
    taps = tap_code_message.split(' ')
    i = 0
    while i < len(taps):
        if taps[i] == '':  # Empty element indicates a space between words
            decoded_message.append(' ')
            i += 1
        else:
            # Convert taps to row and column
            row = len(taps[i])
            col = len(taps[i + 1])
            decoded_message.append(reverse_grid.get((row, col), ''))
            i += 2

    return ''.join(decoded_message)

# Example usage
tap_code_message = ".. ...  . .....  ... .  ... .  ... ....  ... ..  ..... ....  .. ..  .... .....  ..... ...."
decoded_message = decode_tap_code(tap_code_message)

print(f"Encoded Tap Code: {tap_code_message}")
print(f"Decoded Message: {decoded_message}")
