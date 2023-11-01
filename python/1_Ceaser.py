def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if 'a' <= char <= 'z':
            encrypted_message += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted_message += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_message += char
    return encrypted_message

def main():
    message = input("Enter the message to be encrypted:\n")
    shift = int(input("Enter the shift value:\n"))

    encrypted_message = encrypt_message(message, shift)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = encrypt_message(encrypted_message, 26 - shift)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
