import socket, time, threading

global connections;
threads = {};
thread_count = 0;

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
s.listen(3)
while True:
    conn, addr = s.accept()
    conn.send("Welcome..." + str(addr[0]) + ":" + str(addr[1]))
    thread_count = thread_count + 1;
    threads[thread_count] = threading.Thread(target = receive_message, args = (conn,))
    threads[thread_count].start()
#conn.close()
