import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n" 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #opened up a socket here #socket.af_net => ipv4 
                                                                                #socket.sock_stream => tcp
    s.connect((host, port)) #connect to google
    s.send(request) #send request to google
    s.shutdown(socket.SHUT_WR) #I'm done sending data!
    result = s.recv(BYTES_TO_READ) #keep reading the incoming data

    while len(result) > 0:
        print(result)
        result = s.recv(BYTES_TO_READ)
    
    s.close()

#get("www.google.com", 80)
get("localhost", 8080) #for Q6 and Q5
