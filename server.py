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
        print("Welcome "+username)
    else:
        print("Login failed. Invalid username or password.")
        start()
    
def start():
    print()
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
s=so.socket()
s.bind(('localhost',9999))
print('Waiting for connection')
s.listen(1)    
c,addr=s.accept()
print('connected with ',addr)
b=True
while b==True:
    message=c.recv(1024).decode()
    print("Client: ",message )
    if (message.lower()=="bye"):
        c.close()
        print('connection aborted')
        break 

    def f():
        message=input("Give us a sign: ")
        if (message==''):
            f()
        elif(message.lower()=="bye"):
            c.send(message.encode())
            c.close()
            print("Connection aborted")
            return False
        else:
            c.send(message.encode())
        return True
    b=f()
s.close()