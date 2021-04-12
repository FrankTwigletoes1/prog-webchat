import socket

HOST = "147.78.30.122"
PORT = 13000
addr = (HOST, PORT)
UDPSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Enter message to send or type 'exit': ")
    bytedata = str.encode(data)
    UDPSock.sendto(bytedata, addr)

    if data == "exit":
        break

UDPSock.close()


