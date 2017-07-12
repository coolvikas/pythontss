import socket



for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostbyname("iitb.ac.in")
        result = sock.connect((host, port))
        print result
        #print(port)
        if result == 0:
            print ("Port {}: 	 Open",port)
        sock.close()
