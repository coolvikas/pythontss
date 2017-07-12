#localfileserver.py
import socket
port = 60005
s=socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(5)

print('server listening')

while True:
    conn,addr=s.accept()
    print('got connection from',addr)
    data=conn.recv(1024)
    print('server received',repr(data))


    filename='mytext.txt'
    f=open(filename,'rb')
    l=f.read(1024)
    while (l):
        conn.send(l)
        print('sent',repr(l))
        l=f.read(1024)
    f.close()
    print('done sending')
    conn.send('thank u for connection')
    conn.close()
    pass
