import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port=9999

s.connect((host,port))

tm = s.recv(1024)

s.close()

print("the time got from server is %s" % tm.decode
('ascii'))
