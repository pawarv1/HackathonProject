import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# List to keep track of connected clients
clients = []

def broadcast(message, client_socket):
    for client in clients:
        if client['socket'] != client_socket:
            try:
                client['socket'].send(message)
            except:
                client['socket'].close()
                clients.remove(client)

def handle_client(client):
    client_socket = client["socket"]
    try:
        client_socket.send("Welcome to the chatroom! Please enter your name.".encode('utf-8'))
    except:
        client_socket.close()
        clients.remove(client_socket)
        return
    client["name"] = client_socket.recv(1024).decode('utf-8')
    name = client["name"]
    print(f"{name} has joined the chatroom")
        
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Received from {name}: {message.decode('utf-8')}")
                message = f"{name} {message}".encode('utf-8')
                broadcast(message, client)
            else:
                client_socket.close()
                clients.remove(client_socket)
                break
        except:
            client_socket.close()
            clients.remove(client_socket)
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        client = dict(name="John Doe", socket=client_socket, address=client_address)
        clients.append(client)

        print(f"Connection from {client['address']}")
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    main()