import socket
import threading
import sys

class Node:
    def __init__(self, host='localhost', port=8685):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def start(self):
        try:
            threading.Thread(target=self.send_messages).start()
            threading.Thread(target=self.receive_messages).start()
        except:
            self.shutdown()
            print('ERROR occured! Exiting')


    def send_messages(self):
        try:
            while True:
                message = input("Enter message: ")
                self.client_socket.sendall(message.encode())
        except:
            print('OPEN A NEW TERMINAL')
        

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print('')
                    print(f"Received: {message}")
                else:
                    break
            except:
                break
        self.client_socket.close()

    def shutdown(self):
        socketName = self.client_socket.getsockname()
        self.client_socket.close()
        print(socketName," Node shut down")

if __name__ == "__main__":
    newNode = Node()
    newNode.start()

