import socket

HOST = ''
PORT = 12345

SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCK.bind((HOST, PORT))
SOCK.listen(5)

print("Socket aflytter...")

while True:
    CON, ADDR = SOCK.accept()

    print("Forbindelse oprettet fra ", ADDR)

    CON.sendto("Tak for at oprette forbindelse!".encode(), (HOST, PORT))

    print("Modtog besked ", CON.recv(1024), " fra ", ADDR)

SOCK.close()