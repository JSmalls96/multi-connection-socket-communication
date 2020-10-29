#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import re


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("\nWelcome to the chat server!\nNow type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    target_message_re_case = "^/msg.*"
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s!\n\n#! If you ever want to quit, type {exit} to exit.\n#! If you want to private message someone in the chatroom type /msg target the your message' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{exit}", "utf8"):
            if re.match(target_message_re_case, msg.decode("utf8")):
                split = msg.decode("utf8").split(" ",2)
                target_message(split[2], split[1], f"Private message from {name}: ")
            else:
                broadcast(msg, name+": ")
        else:
            client.send(bytes("{exit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

def target_message(msg,tar_name,prefix=""):
    for tar in clients:
        if clients[tar] == tar_name:
            tar.send(bytes(prefix+msg, "utf8"))


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    print(msg)
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = '192.168.56.1'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()