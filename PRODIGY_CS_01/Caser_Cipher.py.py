def caesar_cipher(text, shift, mode):
    result_text = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isupper():
            result_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result_text += char

    return result_text

while True:
    print("Press '1' to encrypt a message & '2' to decrypt a message")
    choice = input("Your choice: ")

    if choice == '1' or choice == '2':
        message = input("Please enter your message: ")
        shift_value = int(input("Enter the shift value: "))
        
        if choice == '1':
            encrypted_message = caesar_cipher(message, shift_value, 'encrypt')
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = caesar_cipher(message, shift_value, 'decrypt')
            print(f"Decrypted message: {decrypted_message}")
        
        break  
    else:
        print("Invalid choice! Please press '1' or '2'.")
