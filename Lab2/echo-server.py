import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1" #IP #lcocalhost
PORT = 8080 #port

def handle_client(conn,addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ) #wait for a request, and when you get it, recive ==> recieves 'b'
            if not data:
                break
            print(data)
            conn.sendall(data)

#Start single threaded echo server
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #intitialize the socket
        s.bind((HOST, PORT)) #binds to the IP, and port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #ignore now for setting it to true #allows us to reuse the port 
        s.listen() #listen for incoming connections
        conn, addr = s.accept() #accepting the client connection #conn = client connection, addr = IP, Port of client
        handle_client(conn,addr) #send it a response!


#Start multi-threaded echo server
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.bind((HOST, PORT)) 
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        s.listen() #allows backlog of up to 2 connections ==> queue [ waiting conn1, conn2 ]
        while True:
            conn, addr = s.accept() 
            thread = Thread(target=handle_client, args=(conn,addr))
            thread.run() 

#start_server()
start_threaded_server()