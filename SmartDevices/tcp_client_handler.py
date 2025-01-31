import socket


class TCPClientHandler:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host: str, port: int):
        """Connect to the TCP server."""
        try:
            self.client_socket.connect((host, port))
            print(f"[TCPClientHandler] Connected to server at {host}:{port}")
        except Exception as e:
            print(f"[TCPClientHandler] Error connecting to server: {e}")

    def send_message(self, message: str):
        """Send a message to the server."""
        try:
            self.client_socket.sendall(f"{message}\n".encode())
            print(f"[TCPClientHandler] Message sent: {message}")
        except Exception as e:
            print(f"[TCPClientHandler] Error sending message: {e}")

    def disconnect(self):
        """Gracefully disconnect from the server."""
        self.client_socket.close()
        print("[TCPClientHandler] Disconnected from server.")