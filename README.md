# PA1

## Setup
* go over IP things
  * why does localhost/127.0.0.1 exist?
  * socket address = IP:portno
  * servers listen on an IP and a port number
  * clients connect from their IP and a random "high numbered" port number (>1023)
* git repo (use azure host for now)
* download ssh private key to `~/.ssh`
* set up `myvm` alias 
* how to `tmux` (for sharing terminal, keep sessions alive)
  * after ssh'ing in, run `tmux attach` to attach to an existing session
  * `CTRL-B d` to dettach

## Protocol
Client program has (4) arguments: HELLO [server IP] [server port#] 
[4-digit connectionID]

Example client usage:
```
$ python3 UDP_client.py HELLO 192.168.0.15 20009 8877
```
The server listens on a port and waits for client connections.

The server receives a client msg and does of the two following responses:

### 1. OK

If connectionID specified by client is not in use, server adds the 
connectionID to its list of in-use IDs and responds with an OK message. 
The OK message starts with the string OK and echoes back the 
connectionID. Also, the server returns client IP and client PORT 
number:
```
OK [ConnectionID] [Client_IP] [Client_Port]
```

For example, if the client IP address is 192.168.0.10, the client port
is 12345, and the connectionID is 9876, the return message from the server
to the client would be 
```
OK 9876 192.168.0.10 12345
```

### 2. ERROR

If connectionID specified by the client is in use, your server responds 
with a RESET message and connectionID . In the case of TCP, your server 
will continue to wait for other clients' requests but will close the 
socket opened by the client that requested this connection. In the UDP 
case, there is no connection to close, and your server will again wait 
for another UDP datagram.

To sum up, the server message is "RESET ConnectionID". For example, if 
the client IP address is 192.168.0.10, the client port is 12345, and the 
connection ID is 9876, the return message from the server would be:
```
RESET 9876
```

## Timeouts
There are two timeout events you need to consider:

### Server Exit Timeout
When your server (whether TCP or UDP) is waiting for a connection request 
but does not receive any requests from any clients for two minutes, your 
server should timeout and exit gracefully after closing any open sockets. 

## ConnectionID Timeout
Your server should timeout and remove connectionIDs that have been in its 
connectionID list for more than 30 seconds. Hint: you can use either 
Python time.time() or Timer Threads. 

 In summary, the steps performed by your server are:

1. Open a socket on a specific port as a server and
2. Listen to the socket (if TCP) or read from that socket (if UDP)
3. Receive a request which consists of a HELLO and a connectionID.
4. Check the connectionID and return the appropriate response to the 
   client, following the rules described above.
5. Handle connectionID 30-second timeouts properly and gracefully exit the
   server if there have been no requests in two minutes.

***

# References
* [Socket Programming in Python](https://realpython.com/python-sockets/)
* [UDP - Client And Server Example](https://pythontic.com/modules/socket/udp-client-server-example)
* [read data from socket](https://stackoverflow.com/questions/43414057/reading-data-from-a-python-socket-received-from-multiple-clients)

