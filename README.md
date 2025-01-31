# TCP Communication Example with SmartDevices module

This project demonstrates the usage of TCP communication using a simple client-server architecture. 
The server and client interact via a callback mechanism defined in the `SmartDevices` module. 
The configuration (IP address and port) is loaded from a `config.json` file.

## Project Structure

- `SmartDevices/`: Contains the core logic for the TCP server and client.
  - `tcp_client_handler.py`: Handles the TCP client functionality (connect, send messages, disconnect).
  - `tcp_server_handler.py`: Handles the TCP server functionality (connect, listen, accept connections, process messages).
  
- `TCPServerApp.py`: Contains the TCP server application logic. Main entry point for the TCP server application. It listens for incoming client connections.
  
- `TCPClientApp.py`: Contains the TCP client application logic. Main entry point for the TCP client application. It connects to the server and sends messages.

- `config.json`: A configuration file containing the host IP and port information for both the client and server.
