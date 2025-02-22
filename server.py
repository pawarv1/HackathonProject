import socket
import threading
import ChatRoom

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# List to keep track of connected clients
clients = []
rooms = []

def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client["socket"].send(message.encode('utf-8'))
            except:
                client["socket"].close()
                clients.remove(client)

def handle_client(client):
    client_socket = client["socket"]
    
    # Receive the client's name
    try:
        client["name"] = client_socket.recv(1024).decode('utf-8')
    except:
        client_socket.close()
        clients.remove(client)
        return
    
    name = client["name"]
    print(f"{name}, {client["address"]} has joined the chatroom")
    client["room"].broadcast(f"{name} has joined the chatroom", client)
        
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received from {name}: {message}")
                client["room"].broadcast(f"[{name}] {message}", client)
            else:
                client_socket.close()
                clients.remove(client)
                print(f"{name} has left the chatroom")
                client["room"].broadcast(f"{name} has left the chatroom", client)
                break
        except Exception as e:
            client_socket.close()
            clients.remove(client)
            print(f"{name} has left the chatroom due to an error: {e}")
            client["room"].broadcast(f"{name} has left the chatroom", client)
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server started on {HOST}:{PORT}")
    room1 = ChatRoom.ChatRoom(1, "Room 1")
    rooms.append(room1)

    while True:
        client_socket, client_address = server.accept()
        client = dict(name="John Doe", room= room1, socket=client_socket, address=client_address)
        clients.append(client)

        room1.add_user(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    main()