def generate_key(text, key):
    key_length = len(key)
    key_generated = ""
    for i in range(len(text)):
        key_generated += key[i % key_length]
    return key_generated

def encrypt(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = (ord(char) + ord(key[i])) % 26
            encrypted_char = chr(shift + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            shift = (ord(char) - ord(key[i]) + 26) % 26
            decrypted_char = chr(shift + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


plaintext = "GEEKSFORGEEKS"
keyword = "AYUSH"

key = generate_key(plaintext, keyword)
ciphertext = encrypt(plaintext, key)

print("Ciphertext: ", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Original/Decrypted Text: ", decrypted_text)
