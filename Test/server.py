import socket

host = "147.78.30.122"
port = 25565
buff = 1024

succ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
succ.bind((host, port))
succ.listen()
conn, addr = succ.accept()

print("Forbindelse fra: ", str(addr))

while True:
    (data, addr) = succ.recv(buff)

    print("Received message:" + data)

    if data == "exit":
        break

    succ.close()