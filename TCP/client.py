import socket

TCP_IP = "192.168.0.23"
TCP_PORT = 5005
BUFFER_SIZE = 1024
pesan = input("Masukkan Pesan Anda : ")

sock = socket.socket(socket.AF_INET, \
    socket.SOCK_STREAM)

sock.connect((TCP_IP, TCP_PORT))
sock.send(pesan.encode())
data = s.recv(BUFFER_SIZE)
sock.close()

print(f"Pesan diterima {data.decode()}")