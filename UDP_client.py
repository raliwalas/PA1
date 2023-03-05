#!/usr/bin/python

import sys      # for command line arg stuff
import socket   # for network stuff

# verify that (4) command line arguments have been passed
n = len(sys.argv)
if n != 5:
    print(f"***ERROR*** You passed " + repr(n-1) + ' arguments. You must pass 4 arguments dood.')
    print("USAGE: ./UDP_client.py HELLO [serverIP] [server port] [connectionID]")
quit()

# Arguments passed
print("\nName of Python script:", sys.argv[0])

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 20009
    addr = (host, port)

    """ Creating the UDP socket """
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data = input("Enter a word: ")

        if data == "!EXIT":
            data = data.encode("utf-8")
            client.sendto(data, addr)

            print("Disconneted from the server.")
            break

        data = data.encode("utf-8")
        client.sendto(data, addr)

        data, addr = client.recvfrom(1024)
        data = data.decode("utf-8")
        print(f"Server: {data}")

