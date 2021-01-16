#server
import socket

s = socket.socket()
print("Socket created")

s.bind(('Localhost',9999))

s.listen(5)  #it can connect 5 clients
print("Waiting for connections")

while True:
    c,addr = s.accept()
    print(c.recv(1024).decode())
    print("Connected with", addr)

    c.send(bytes('Welcome to the server','utf-8'))
    c.send(bytes('Waiting for someone to connect', 'utf-8'))

    c.close()
    
    
#client
import socket

c = socket.socket()

c.connect(('localhost',9999))

name = input("Enter your name:")
c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())
print(c.recv(1024).decode())
