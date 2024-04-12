def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Convert the character to its ASCII code
            ascii_code = ord(char)
            
            # Shift the ASCII code by the key value
            shifted_code = (ascii_code - ord('A' if is_upper else 'a') + key) % 26
            
            # Convert the shifted code back to a character
            shifted_char = chr(shifted_code + ord('A' if is_upper else 'a'))
            
            # Append the shifted character to the result
            result += shifted_char
        else:
            # If the character is not an alphabet letter, leave it unchanged
            result += char
    
    return result

def caesar_decrypt(ciphertext, key):
    # Decryption is just encryption with a negative key
    return caesar_encrypt(ciphertext, -key)

# Example usage:
plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key (an integer): "))

ciphertext = caesar_encrypt(plaintext, key)
decrypted_message = caesar_decrypt(ciphertext, key)

print("Encrypted message:", ciphertext)
print("Decrypted message:", decrypted_message)