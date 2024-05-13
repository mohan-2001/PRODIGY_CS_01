def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result

def main():
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, -shift)
            print(f"Decrypted message: {decrypted_message}")
        else:
            print("Invalid choice. Please choose 1 for encryption or 2 for decryption.")

if __name__ == "__main__":
    main()