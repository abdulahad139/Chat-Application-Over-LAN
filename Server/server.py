import socket
import threading


SERVER_HOST = 'Server_IP' # ipv4 address of the server  
SERVER_PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_HOST, SERVER_PORT))
server.listen()
print(f"Server is listening on {SERVER_HOST}:{SERVER_PORT}")

clients = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"Received message: {message.decode('utf-8')}")
            broadcast(message, client) 
        except:
            clients.remove(client)
            client.close()
            break


def receive_clients():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        clients.append(client)
        client.send("Welcome to the chat!".encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


server_thread = threading.Thread(target=receive_clients)
server_thread.start()

while True:
    command = input("Type 'exit' to stop the server: ")
    if command.lower() == 'exit':
        print("Shutting down the server.")
        for client in clients:
            client.close()
        server.close()
        break
