#localfileclient.py

import socket
s=socket.socket()
host = socket.gethostname()
port = 60005
s.connect((host,port))
s.send("hello srever !!")

with open('received_file','wb') as f:
    print('file opened')
    while True:
        print('recieving data....')
        data=s.recv(1024)
        print('data=%s',(data))
        if not data:
            break
        f.write(data)
        pass
f.close()
print('successfully got the file')
s.close()
print('connection closed')
