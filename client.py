#!/usr/bin/env python3
import socket
from threading import Thread
import hashlib


def receive():
    while True:
        msg = client_socket.recv(BUFSIZ).decode("utf8")
        if msg == "{exit}":
            client_socket.close()
            break
        if not msg:
            break
        print(msg)


def send():
    while True:
        msg = input()
        # encoded = hashlib.sha256(bytes(msg, "utf8"))
        # ciphertext = encoded.hexdigest()
        # print(ciphertext)
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{exit}":
            break

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