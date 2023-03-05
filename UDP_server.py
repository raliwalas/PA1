#!/usr/bin/python

import socket

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# listens on all interfaces
# can listen on just one by specifying the IP in the first argument
serverSocket.bind(('', serverPort))

print("The server is ready to receive.")

while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode().upper()
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)

