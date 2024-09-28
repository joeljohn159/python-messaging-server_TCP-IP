import socket
import threading
import queue

class Server:
    def __init__(self, host='localhost', port=8685):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.clients = {}
        self.buffer = queue.Queue()
        self.running = True
        self.counter = 0

    def start(self):
        print("Server (",self.host,") started on port", self.port)
        threading.Thread(target=self.handle_clients).start()
        threading.Thread(target=self.forward_messages).start()

    def handle_clients(self):
        while self.running:
            try:
                self.counter += 1
                client_socket, client_address = self.server_socket.accept()
                print(f"Client {client_address} connected")
                self.clients[self.counter] = [client_address,client_socket]
                threading.Thread(target=self.receive_messages, args=(client_socket, client_address)).start()
            except OSError:
                break

    def receive_messages(self, client_socket, client_address):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"Received from {client_address}: {message}",end="")
                    self.buffer.put((client_address, message))
                else:
                    break
            except:
                break
        client_socket.close()
        del self.clients[client_address]
        print(f"Client {client_address} disconnected")

    def forward_messages(self):
        while True:
            if not self.buffer.empty():
                client_address, message = self.buffer.get()
                for address, client_socket in self.clients.values():
                    if address != client_address:
                        client_socket.sendall(message.encode())

    def servershutdown(self):
        self.running = False
        self.server_socket.close()
        print("Server shut down")
