import json
import os
from SmartDevices.tcp_client_handler import TCPClientHandler


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as config_file:
        return json.load(config_file)


if __name__ == "__main__":
    config = load_config()
    host = config["host"]
    port = config["port"]

    client_handler = TCPClientHandler()
    client_handler.connect(host, port)

    try:
        while True:
            message = input("Enter message (type 'exit' to quit): ")
            if message.lower() == "exit":
                break
            client_handler.send_message(message)
    finally:
        client_handler.disconnect()