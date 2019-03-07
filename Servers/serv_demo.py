import socket
host = socket.gethostbyname(socket.gethostname())
port = 4000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("Started serveron port: ",port)
s.listen(1)
c,addr = s.accept()
print("Connected from: ",addr)
s.send("Bye".encode())