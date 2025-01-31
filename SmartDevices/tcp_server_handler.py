import socket
from typing import Callable


class TCPServerHandler:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None
        self.client_address = None
        self.message_callback: Callable[[str], None] = None

    def start(self, host: str, port: int):
        """Start the TCP server and bind to the given IP and port."""
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)
        print(f"[TCPServerHandler] Server started at {host}:{port}")

    def accept_client(self):
        """Accept a single client connection."""
        self.client_socket, self.client_address = self.server_socket.accept()
        print(f"[TCPServerHandler] Connection established with {self.client_address}")

    def read_messages(self):
        """Continuously read messages from the client (blocking call)."""
        if not self.client_socket:
            print("[TCPServerHandler] No client connected.")
            return
        try:
            while True:
                data = self.client_socket.recv(1024).decode().strip()
                if not data:
                    print("[TCPServerHandler] Client disconnected.")
                    break
                if self.message_callback:
                    self.message_callback(data)
        except Exception as e:
            print(f"[TCPServerHandler] Error reading messages: {e}")

    def send_message(self, message: str):
        """Send a message to the connected client."""
        if self.client_socket:
            self.client_socket.sendall(f"{message}\n".encode())
            print(f"[TCPServerHandler] Message sent: {message}")
        else:
            print("[TCPServerHandler] No client connected to send a message.")

    def register_callback(self, callback: Callable[[str], None]):
        """Register a callback for received messages."""
        self.message_callback = callback

    def stop(self):
        """Gracefully stop the server."""
        if self.client_socket:
            self.client_socket.close()
        self.server_socket.close()
        print("[TCPServerHandler] Server stopped.")