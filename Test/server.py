import socket

HOST = "147.78.30.122"
PORT = 25565

succ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
succ.bind((HOST, PORT))
succ.listen(1)
conn, addr = succ.accept()

print("Afventer besked...")

while True:
    data = succ.recv(1024)

    print("Received message:" + data)

    if data == "exit":
        break

    succ.close()