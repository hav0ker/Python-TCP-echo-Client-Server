import socket 

ip = "127.0.0.1"
port = 40674

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

cMsg = input("type your message for the server here: ")
data = bytes(cMsg, "utf-8")

print(f"sending message to {ip} port {port}")
s.sendall(data)

serverData = str(s.recv(1024))
print("message recieved from the server: ", str(serverData))