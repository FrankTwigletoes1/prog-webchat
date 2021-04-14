import socket

HOST = '127.0.0.1'
PORT = 12345

SOCK = socket.socket()
SOCK.connect((HOST, PORT))

while True:
    print(SOCK.recv(1024))
    
    data = input("Enter message to send or type 'exit': ")

    if data == "exit":
        break
    else:
        SOCK.sendto(data.encode(), (HOST, PORT))

SOCK.close()