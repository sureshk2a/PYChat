import socket
client_s = socket.socket()
#ip_to_connect = input("Which IP do you wanna connect to? :")
#client_s.connect((ip_to_connect,4000))
client_s.connect(('localhost',4000))
msg = client_s.recv(1024)
#Loop as long as there is a message to receive
while msg:
    print("Received",msg.decode())
    msg = client_s.recv(1024)
client_s.close()

