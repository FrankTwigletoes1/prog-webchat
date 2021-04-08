import socket, sys, threading

class Server(threading.Thread):
    def __init__():
        threading.Thread.__init__(self)
        self.running    = True
        self.connection = None
        self.adress     = None
        self.socket     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        host = '85.129.54.45' # Emils ip fuck af
        port = 25565

        self.socket.bind((host,port))
        self.socket.listen(1)
        self.connection, self.adress = self.socket.accept()

        while self.running:
            inputR, outputR, excepR = select.select([self.connection], [self.connection], [])

            for i in inputR:
                msg = self.connection.resv(1024)

                if msg:
                    print("{0}: {1}").format(self.adress, msg)
                else: break

    def shino(self):
        self.running = False

class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.host = None
        self.socket = None
        self.running = True

    def run(self):
        port = 25565
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, port))
        
        while self.running:
            inputR, outputR, excepR = select.select([self.connection], [self.connection], [])

            for i in inputR:
                msg = self.socket.resv(1024)

                if msg:
                    print("{0}: {1}").format("Myself", msg)
                else: break

    def shino(self):
        self.running = False

class textInput(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
    
    def run(self):
        while self.running:
            msg = input("")
            try:
                Client.socket.sendall(text)
            except:
                Exception


    def shino(self):
        self.running = False

