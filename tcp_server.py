import socket

port = 40674
s_addr = ('127.0.0.1', port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(s_addr)
print("server up and listening")
s.listen(5)

c, addr = s.accept()
print("connection from ", addr)

while True:
    cData = c.recv(1024)
    if not cData:
        break
    c.sendall(cData)
        
