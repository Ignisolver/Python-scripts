import socket

soc = socket.socket()

PORT = 1234
soc.bind(('',PORT))
file = open(r'C:\Users\ignsz\Desktop\pliki.zip', 'wb')
soc.listen()
print("server listing")
while True:
    conn, addr = soc.accept()
    rec_data = conn.recv(1024)
    n = 0
    while rec_data:
        file.write(rec_data)
        rec_data = conn.recv(1024)
        print(n)

    file.close()
    conn.close()
    print("operation success")
