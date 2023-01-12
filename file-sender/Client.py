import socket
s = socket.socket()
PORT = 1234
s.connect(("192.168.1.19", PORT))
file = open("filmy.zip", 'rb')
data2send = file.read(1024)
while data2send:
    s.send(data2send)
    data2send = file.read(1024)
file.close()
s.close()