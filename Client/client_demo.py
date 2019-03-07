import socket
client_s = socket.socket()
msg = client_s.recv(1024)
while msg:
    print("Received",msg.decode())
    msg = client_s.recv(1024)
client_s.close()

