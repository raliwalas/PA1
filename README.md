# PA1

## Protocol
Client program has (4) arguments: HELLO [server IP] [server port#] [4-digit connectionID]

Example client usage:
```
  $ python3 UDP_client.py HELLO 192.168.0.15 20009 8877
```
The server listens on a port and waits for client connections.

The server receives a client msg and does of the two following responses:

