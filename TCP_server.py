import socket

# create socket object
# AF_INET indicates IPv4
# SOCK_STREAM indicates TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to tuple (IP:portno) - listen on TCP port 20009
s.bind((socket.gethostname(), 20009))

# listen but only queue up 5 connections
s.listen(5)

while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
        clientsocket.send(bytes("Welcome motherfucker!", "utf-8"))
