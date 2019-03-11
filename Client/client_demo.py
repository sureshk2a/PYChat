import socket, threading
# ip_to_connect = input("Which IP do you wanna connect to? :")
# client_s.connect((ip_to_connect,4000))
client_s = socket.socket()

def receive_message(client_s):
    while True:
        msg = client_s.recv(1024)
        if len(msg.decode()) > 2:
            print ("Received", msg.decode())

def message():
    client_s.connect(('localhost', 4000))
    t1 = threading.Thread(target = receive_message, args=(client_s,))
    t1.start()
    while True:
        inp = raw_input();
        client_s.send(inp)
    return client_s

cl_conn = message()
cl_conn.close()
