#echo_client.py
import socket

host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))

s.sendall(b'HELLO,WORLD')

data = s.recv(1024)
s.close()

print('received',(data))
