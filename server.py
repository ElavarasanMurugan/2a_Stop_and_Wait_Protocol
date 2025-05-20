import socket

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(1)
print("Server is running...")

conn, addr = s.accept()
print("Connected to", addr)

while True:
    data = conn.recv(1024).decode()
    if data == "END":
        break
    print("Received:", data)
    conn.send("ACK".encode())

conn.close()
s.close()