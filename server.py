import socket
import threading
import ChatRoom

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# List to keep track of connected clients
clients = []
rooms = []

def handle_client(client):
    client_socket = client["socket"]
    room = client["room"]
    
    # Receive the client's name
    try:
        client["name"] = client_socket.recv(1024).decode('utf-8')
    except:
        clients.remove(client)
        room.remove_user(client)
        return
    
    name = client["name"]
    print(f"{name}, {client["address"]} has joined the chatroom")
    room.broadcast(f"{name} has joined the chatroom", client)
        
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received from {name}: {message}")
                room.broadcast(f"[{name}] {message}", client)
            else:
                clients.remove(client)
                room.remove_user(client)
                break
        except Exception as e:
            clients.remove(client)
            room.remove_user(client)
            print(f"{name} has left the chatroom due to an error: {e}")
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