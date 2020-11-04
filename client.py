#!/usr/bin/env python3
import socket
from threading import Thread
import re


def encrypt(text, s):
    result = ""
    
    # traverse text
    for i in range(len(text)):
        char = text[i]

        # encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif (char.islower()): #encrypt lowercase characters
            result += chr((ord(char) + s - 97) % 26 +97)
        else: #special character
            result += chr((ord(char) + s - 32) % 26 + 32)
    
    return result

def decrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # decrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        # decrypt lowercase characters
        elif (char.islower()):
            result += chr((ord(char) - s - 97) % 26 + 97)
        else: #special character
            result += chr((ord(char) - s - 32) % 26 + 32)

    return result

def receive():
    counter = 0
    while True:
        msg = client_socket.recv(BUFSIZ).decode("utf8")
        # message doesn't exist
        if not msg:
            break
        
        # if exitting
        if msg == "{exit}":
            client_socket.close()
            break

        # if it is not a starting message
        if counter >= 2 and ":" in msg:
            split = msg.split(":",1)
            msg = split[0].strip() +": "+decrypt(split[1].strip(), 2)

        print(msg)
        counter += 1





def send():
    firstMessage = True
    private_msg_re_case = "^/msg.*"

    while True:
        msg = input()
        if msg == "{exit}" and not firstMessage:
            client_socket.send(bytes(msg, "utf8"))
            break
        
        if firstMessage:
            client_socket.send(bytes(msg, "utf8"))
            firstMessage = False
        else:
            cipher = ""
            # if message being sent is a private message
            if re.match(private_msg_re_case, msg):
                split = msg.split(" ",2)
                cipher = split[0] +" "+split[1] + " "+ encrypt(split[2].strip(), 2)
            else:
                cipher = encrypt(msg.strip(),2)
            client_socket.send(bytes(cipher, "utf8"))
        
        

SELECTION = input('Would you like to connect to a \n1. LAN Server\n2. Public Server\n')
if int(SELECTION) == 1:
    HOST = socket.gethostbyname(socket.gethostname())
else:
    print(SELECTION)
    HOST = input('Enter host: ')

PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)


receive_thread = Thread(target=receive)
send_thread = Thread(target=send)
receive_thread.start()
send_thread.start()
receive_thread.join()
send_thread.join()