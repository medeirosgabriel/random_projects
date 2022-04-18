import socket
from threading import Thread

clients_sockets = []

def broadcast(message, connection):
    print("OK")
    for client in clients_sockets:
        if (client != connection):
            client.sendall(message.encode())

class ClientThread(Thread):
	
    def __init__(self,clientAddress,clientSocket):
        Thread.__init__(self)
        self.socket = clientSocket
        self.address = clientAddress
        print("New connection: ", clientAddress)
        broadcast("User at " + str(self.address) + " connected...", self.socket)
        
    def run(self):
        while True:
            data = self.socket.recv(1024)
            if not data or data.decode() == 'BYE':
                msg = "User at " + str(self.address) + " disconnected..."
                broadcast(msg, self.socket)
                clients_sockets.remove(self.socket)
                self.socket.close()
                print(msg)
                break
            else:
                msg = str(self.address) + ": " + data.decode()
                broadcast(msg, self.socket)
                print(msg)

LOCALHOST = "127.0.0.1"
PORT = 8090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((LOCALHOST, PORT))
except:
    server.bind((LOCALHOST, PORT + 1))

print("--------------------------------- Chat started ---------------------------------")
while True:
    server.listen(1)
    clientSocket, clientAddress = server.accept()
    clients_sockets.append(clientSocket)
    newthread = ClientThread(clientAddress, clientSocket)
    newthread.start()