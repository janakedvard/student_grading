import sys
import socket
import struct
import select
import random

neptun_addr = 'localhost'
neptun_port = 10003

#server_address = ((server_addr, server_port))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((neptun_addr, neptun_port))

student_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        data, client_addr = sock.recvfrom(1024)
        student_addr = 'localhost'
        student_port = data.decode()
        print("student port:", student_port)
        grade = random.randint(1,5)
        student_sock.sendto(grade.encode(), (student_addr, student_port))
        print("elküldve:", grade)
    except KeyboardInterrupt:
        break
        
sock.close()
print("Server terminated")