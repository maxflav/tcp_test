import random
import socket
import sys
import threading
import time

def sending(sock):
    while True:
        message = input('')
        sock.sendall(message.encode('utf-8'))

def receiving(sock):
    while True:
        print(sock.recv(1024).decode('utf-8'))


if len(sys.argv) < 2:
    print("Specify a port")
    exit(1)

port = int(sys.argv[1])

sock = socket.socket()
sock.connect(('localhost', port))

try:
    send_thread = threading.Thread(target=sending, args=(sock,))
    send_thread.daemon = True
    send_thread.start()

    receiving(sock)
finally:
    sock.close()

