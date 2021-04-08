import socket

HOST = "147.78.30.122"
PORT = 25565

succ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
succ.bind((HOST, PORT))
succ.listen()
conn, addr = succ.accept()

print("Forbindelse fra: ", str(addr))

while True:
    (data, addr) = succ.recv(1024)

    print("Received message:" + data)

    if data == "exit":
        break

    succ.close()