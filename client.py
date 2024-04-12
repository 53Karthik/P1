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
def playfair_cipher(plaintext, key, mode):  
    # Define the alphabet, excluding 'j'  
    alphabet = 'abcdefghiklmnopqrstuvwxyz'  
    key = key.lower().replace(' ', '').replace('j', 'i')  
    # Construct the key square  
    key_square = ''  
    for letter in key + alphabet:  
        if letter not in key_square:  
            key_square += letter  
    # Split the plaintext into digraphs, padding with 'x' if necessary  
    plaintext = plaintext.lower().replace(' ', '').replace('j', 'i')  
    if len(plaintext) % 2 == 1:  
        plaintext += 'x'  
    digraphs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]  

    def encrypt(digraph):  
        a, b = digraph  
        row_a, col_a = divmod(key_square.index(a), 5)  
        row_b, col_b = divmod(key_square.index(b), 5)  
        if row_a == row_b:  
            col_a = (col_a + 1) % 5  
            col_b = (col_b + 1) % 5  
        elif col_a == col_b:  
            row_a = (row_a + 1) % 5  
            row_b = (row_b + 1) % 5  
        else:  
            col_a, col_b = col_b, col_a  
        return key_square[row_a*5+col_a] + key_square[row_b*5+col_b]  
    
    def decrypt(digraph):  
        a, b = digraph  
        row_a, col_a = divmod(key_square.index(a), 5)  
        row_b, col_b = divmod(key_square.index(b), 5)  
        if row_a == row_b:  
            col_a = (col_a - 1) % 5  
            col_b = (col_b - 1) % 5  
        elif col_a == col_b:  
            row_a = (row_a - 1) % 5  
            row_b = (row_b - 1) % 5  
        else:  
            col_a, col_b = col_b, col_a  
        return key_square[row_a*5+col_a] + key_square[row_b*5+col_b]  

    result = ''  
    for digraph in digraphs:  
        if mode == 'encrypt':  
            result += encrypt(digraph)  
        elif mode == 'decrypt':  
            result += decrypt(digraph)  
  
    # Return the result  
    return result  
def encryptRailFence(text, key):

    rail = [['\n' for i in range(len(text))]
                for j in range(key)]
     
    # to find the direction
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
         
        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1
         
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
def decryptRailFence(cipher, key):
 
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix to
    # distinguish filled spaces
    # from blank ones
    rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]
     
    # to find the direction
    dir_down = None
    row, col = 0, 0
     
    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        # place the marker
        rail[row][col] = '*'
        col += 1
         
        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
             
    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
            (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
         
        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

usernames = []
passwords = []

def register():
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")
    usernames.append(username)
    passwords.append(password)
    print("Registration successful.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in usernames and passwords[usernames.index(username)] == password:
        print("Login successful.")
    else:
        print("Login failed. Invalid username or password.")
        start()
    
def start():
    print("Press 1 to register\nPress 2 to login")
    choice=input()
    if choice=='1':
        register()
        login()
    elif choice=='2':
        login()
    else:
        print("Enter valid choice")
        start()

start()

import socket as so

s = so.socket()
s.connect(('localhost', 9999))

b = True
while b:
    message = input("Enter message: ")
    if message == '':
        continue
    print("Enter key\n(1 to encrypt in Caesar cipher\n2 to encrypt in playfair cipher\n3 to encrypt in railfence cipher\n")
    s.send(message.encode())

    if message.lower() == "bye":
        print("Connection closed by client")
        break

    response = s.recv(1024).decode()
    print("Server's message:", response)

    if response.lower() == "bye":
        print("Connection closed by server")
        break

s.close()
