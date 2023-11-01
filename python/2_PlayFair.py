def playfair_encrypt(plaintext, key):
    def build_key_matrix(key):
        key = key.replace('J', 'I')
        key = ''.join(sorted(set(key), key=key.index))
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        matrix = list(key)
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)
        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_position(letter, matrix):
        for i, row in enumerate(matrix):
            if letter in row:
                return i, row.index(letter)
        return None  # Handle characters not found in the matrix

    def encrypt_pair(pair, matrix):
        pos1 = find_position(pair[0], matrix)
        pos2 = find_position(pair[1], matrix)

        if pos1 is not None and pos2 is not None:
            if pos1[0] == pos2[0]:  # Same row
                return matrix[pos1[0]][(pos1[1] + 1) % 5] + matrix[pos2[0]][(pos2[1] + 1) % 5]
            elif pos1[1] == pos2[1]:  # Same column
                return matrix[(pos1[0] + 1) % 5][pos1[1]] + matrix[(pos2[0] + 1) % 5][pos2[1]]
            else:  # Different row and column
                return matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
        else:
            return None

    key_matrix = build_key_matrix(key)
    plaintext = plaintext.upper().replace('J', 'I')
    duets = [plaintext[i:i + 2] if i + 1 < len(plaintext) and plaintext[i] != plaintext[i + 1] else plaintext[i] + 'X' for i in range(0, len(plaintext), 2)]
    encrypted_text = ''.join(encrypt_pair(duet, key_matrix) for duet in duets if encrypt_pair(duet, key_matrix) is not None)
    return encrypted_text

base = 'monarchy'
plaintext = 'instruments'

encrypted_text = playfair_encrypt(plaintext, base)
print('Encrypted Text:', encrypted_text)