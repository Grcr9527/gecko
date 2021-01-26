#!/usr/bin/python3

import socket
import threading

bind_IP = "127.0.0.1"
bind_port = 9001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_IP, bind_port))
server.listen(5)
print("[*] Listening on", (bind_IP, bind_port))


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Received:", request)
    str = 'ACK!'
    str = str.encode()
    client_socket.send(str)
    client_socket.close()

while True:
    client, addr = server.accept()
    print("[*] Accepted connection from :", (addr[0], addr[1]))
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
