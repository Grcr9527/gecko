#!/usr/bin/python3

import socket

target_IP = "127.0.0.1"
target_port = 9001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_IP, target_port))

str = 'FUVK!'
str = str.encode()
client.send(str)

response = client.recv(1024).decode('gbk')

print(response)
