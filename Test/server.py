import os 
from socket import *
host = "".
port = 80
buff = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")

while True:
    (data, addr) = UDPSock.recvfrom(buff)
    print("Received message:" + data)
    if data == "exit":
        break
    UDPSock.close()
    os._exit(0)

    du en cuck