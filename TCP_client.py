import socket

# create socket object
# AF_INET indicates IPv4
# SOCK_STREAM indicates TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# this connects to localhost (gethostname) - for testing
s.connect((socket.gethostname(), 20009))

# receive a fixed qty of bytes (1024)
msg = s.recv(1024)

# decode and print the bytes
print(msg.decode("utf-8"))



