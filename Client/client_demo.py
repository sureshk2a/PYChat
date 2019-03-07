import socket
# ip_to_connect = input("Which IP do you wanna connect to? :")
# client_s.connect((ip_to_connect,4000))
client_s = socket.socket()
def message():
    client_s.connect(('localhost', 4000))
    msg = client_s.recv(1024)
    while msg:
        print("Received", msg.decode())
        msg = client_s.recv(1024)
    return client_s
cl_conn = message()
cl_conn.close()

