import socket, time, threading

global connections;                            #-----SERVER-------
threads = {};
thread_count = 0;
host,port = 'localhost',4000

def receive_message(conn):
    while True:
        msg = conn.recv(1024)
        while msg:
            print(msg.decode)
            conn.send("Received by: ",host)
            if msg.decode() == "exit":
                conn.close()
                threading._shutdown()

#host,port = socket.gethostbyname(socket.gethostname()),4000

  #Using localhost addr for now

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
connections  = {};
print("Started server on : ",host," : ",port)
s.listen(3)
while True:
    conn, addr = s.accept()
    conn.send(b"Welcome...: " + str(addr[0]).encode() + b" : " + str(addr[1]).encode())
    thread_counts = thread_count + 1;
    threads[thread_count] = threading.Thread(target = receive_message(conn,))
    threads[thread_count].start()
#conn.close()
