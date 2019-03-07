import socket
#host,port = socket.gethostbyname(socket.gethostname()),4000
host = 'localhost' #Using localhost addr for now
port = 4000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("Started server on : ",host,":",port)
s.listen(1)
c,addr = s.accept()
print("Connected from: ",addr)
s.send("Hai im Pewds".encode())
s.close()