import socket
import sys
import threading

class Server(threading.Thread):
    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '85.129.54.45' # Emils ip fuck af
        port = 25565
        self.socket.bind((host, port))
        self.socket.listen(1)
        print("Looking at host and port: ", host," ", port)



class Client(threading.Thread):
    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
