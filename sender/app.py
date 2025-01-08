import socket
import time

HOST = "receiver"
PORT = 5000

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b"Hello from Sender!")
            print("Message sent.")
            time.sleep(5)
    except Exception as e:
        print("Retrying connection:", e)
        time.sleep(5)