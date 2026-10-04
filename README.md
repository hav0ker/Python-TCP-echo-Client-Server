# Python-TCP-echo-Client-Server
A minimal TCP socket example in Python: a server that echoes back whatever a client sends it.
## Files

- `server.py` — listens for a connection and echoes back any data it receives
- `client.py` — connects to the server, sends a typed message, and prints the reply

## How it works

1. The server binds to `127.0.0.1:40674` and waits for one client to connect.
2. The client connects, prompts you to type a message, and sends it as bytes.
3. The server receives the bytes and sends them straight back (`c.sendall(cData)`).
4. The client prints whatever came back.
5. When the client closes its socket, the server detects the empty read (`recv` returns `b''`), breaks its loop, and exits.

Both programs only run once per connection — after one message round-trip, the client exits, the server notices the disconnect, and the server exits too.
Handles **one connection only**!!!
## Requirements

- Python 3 (no external packages — uses only the built-in `socket` module)
## Usage

### Terminal 1

`python server.py`

### Terminal 2

`python client.py`
