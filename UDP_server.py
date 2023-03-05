import socket

if __name__ == "__main__":
    #host = "127.0.0.1"
    port = 20009

    # Creating the UDP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the host address with the port ("" indicates listen on all interfaces)
    #server.bind((host, port))
    server.bind(("", port))

    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")
        print(data)

        if data == "!EXIT":
            print("Client disconnected.")
            break

        print(f"Client: {data}")

        data = data.upper()
        data = data.encode("utf-8")
        server.sendto(data, addr)

