#!/usr/bin/python3

import socket

target_IP = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

str = 'AAABBBCCCDDDFFF'
str = str.encode()

client.sendto(str,(target_IP, target_port))

data,addr=client.recvfrom(4096)
print(data)


print(response)
