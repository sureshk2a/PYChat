import socket, time, threading

def receive_message(conn):
    while True:
        msg = conn.recv(1024)
        if len(msg.decode()) > 2:
            print ("Received", msg.decode())
            conn.send("Roger That : "+msg.decode())
            if msg.decode() == "exit":
                conn.close()
                threading._shutdown()

#host,port = socket.gethostbyname(socket.gethostname()),4000
host = 'localhost' #Using localhost addr for now
port = 4000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
connections  = {};
print("Started server on : ",host,":",port)
s.listen(1)
conn,addr = s.accept()
conn.send("Welcome...")
t2 = threading.Thread(target = receive_message, args = (conn,))
t2.start()
#conn.close()
