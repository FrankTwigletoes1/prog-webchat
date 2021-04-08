import os
from socket import * 
host = "147.78.30.122"
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input("Enter message to send or type 'exit': ")
    bytedata = str.encode(data)
    UDPSock.sendto(bytedata, addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)


