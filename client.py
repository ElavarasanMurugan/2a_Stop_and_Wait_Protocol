import socket

s = socket.socket()
s.connect(('localhost', 8000))

n = int(input("Enter number of frames to send: "))

for i in range(n):
    frame = f"Frame {i+1}"
    s.send(frame.encode())
    print("Sent:", frame)

    ack = s.recv(1024).decode()
    print("Received:", ack)

s.send("END".encode())
s.close()