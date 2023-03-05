#!/usr/bin/python

import sys      # for command line arg stuff
import socket   # for network stuff

# verify that (4) command line arguments have been passed
n = len(sys.argv)
if n != 5:
    print(f"ERROR: You passed " + repr(n-1) + ' arguments. You must pass 4 arguments dood.')
    print("USAGE: ./UDP_client.py HELLO [serverIP] [server port] [connectionID]")
    quit()

# show arguments passed
print("--------------------------------")
print("script name:	", sys.argv[0])
print("String:		", sys.argv[1])
print("server IP:	", sys.argv[2])
print("server port:	", sys.argv[3])
print("connectionID:	", sys.argv[4])
print("--------------------------------")

msgFromClient     = sys.argv[1]
bytesToSend       = str.encode(msgFromClient)
serverAddressPort = (sys.argv[2], int(sys.argv[3]))	### note string to int conversion
bufferSize        = 1024

# create UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])
print(msg)
