import socket
import sys
import threading

all_clients = []
if len(sys.argv) < 2:
    print("Specify a port")
    exit(1)

port = int(sys.argv[1])

def await_new_connections():
    try:
        sock = socket.socket()
        sock.bind(('localhost', port))
        sock.listen(5)
        while True:
            client, client_address = sock.accept()
            all_clients.append(client)

            new_thread = threading.Thread(target=handle_client, args=(client, all_clients))
            new_thread.daemon = True
            new_thread.start()

    finally:
        print("Shutting down")
        for client in all_clients:
            client.close()
        sock.close()

def handle_client(client, all_clients):
    try:
        while True:
            data = client.recv(1024)
            print(data.decode('utf-8'))
            if not data:
                return

            for output_client in all_clients:
                if output_client != client:
                    output_client.sendall(data)

    finally:
        client.close()
        all_clients.remove(client)

await_new_connections()
