from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import sys
import struct
import random
server_addr = ('localhost', 10002)

server = socket(AF_INET, SOCK_STREAM)

id = random.randint(10002, 10100)

client_addr = 'localhost'
client_port = id
client = socket(AF_INET, SOCK_DGRAM)


days = [1,8,15,22,29]
choosen_day = random.choice(days)

msg = bytes(str(id) +" "+ str(choosen_day), 'utf-8')    
server.connect(server_addr)
server.sendall(msg)
print("elküldve:", id, choosen_day)
msg = server.recv(1024)
print (msg.decode())
if msg.decode() == "ELFOGAD":
    client.bind((client_addr, client_port))
    data, client_address = client.recvfrom(1024)
    print(data.decode())
server.close()