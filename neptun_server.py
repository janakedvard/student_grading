import sys
import socket
import struct
import select

num_of_students = dict()
num_of_students[sys.argv[1]] = int(sys.argv[2])
num_of_students[sys.argv[3]] = int(sys.argv[4])
num_of_students[sys.argv[5]] = int(sys.argv[6])
num_of_students[sys.argv[7]] = int(sys.argv[8])
num_of_students[sys.argv[9]] = int(sys.argv[10])


server_addr = 'localhost'
server_port = 10002


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind( (server_addr, server_port) )

sock.listen(5)




inputs = [ sock ]

while True:
    try:
        readables, _, _ = select.select( inputs, [], [] )
        
        for s in readables:
            if s is sock:
                connection, client_info = sock.accept()
                print("Csatlakozott valaki: %s:%d" % client_info )
                inputs.append(connection)
            else:
                msg = s.recv(1024)
                if not msg:
                    s.close()
                    print("A kliens lezárta a kapcsolatot")
                    inputs.remove(s)
                    continue
                parsed_msg = msg.decode().split(" ")
                print ('üzenet:', parsed_msg[0]," ", parsed_msg[1])
                
                answer = ""
                
                if num_of_students[parsed_msg[1]] + 1 <=10:
                    answer = b'ELFOGAD'

                else:
                    answer = b'ELUTASIT'
                s.sendall(answer)
                print("elküldve: ", answer.decode())
                
                
			
    except:
        for s in inputs:
            s.close()
        print("Server closing")
        break