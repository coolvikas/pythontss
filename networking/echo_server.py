#echo_server.py

import socket

host = ''
port = 12345

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)

connection,addr = s.accept()
print('connected by',addr)

while True:
    data=connection.recv(1024)
    if not data:
        break
    connection.sendall(data)
    pass
connection.close()
