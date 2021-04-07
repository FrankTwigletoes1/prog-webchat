import socket

def server():
    host = '147.78.30.122'
    port = 80
    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    
    while True:
        data = c.recv(1024)
        if not data:
            break
            
        data = str(data).upper()
        c.send(data)
    c.close

def client():
    host = '147.78.30.122'
    port = 80
    s = socket.socket()
    s.connect((host, port))
    message = input("->")
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        message = input("->")
    s.close

