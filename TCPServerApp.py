import json
import os
from SmartDevices.tcp_server_handler import TCPServerHandler


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as config_file:
        return json.load(config_file)


def on_message_received(message: str):
    print(f"Server received: {message} (This message is created from callback)")


if __name__ == "__main__":
    config = load_config()
    host = config["host"]
    port = config["port"]

    server_handler = TCPServerHandler()
    server_handler.start(host, port)

    server_handler.register_callback(on_message_received)

    try:
        server_handler.accept_client()
        server_handler.read_messages()
    except KeyboardInterrupt:
        print("[Main] Server shutting down.")
    finally:
        server_handler.stop()