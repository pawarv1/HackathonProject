import socket
import threading
import ChatRoom

class Server:
    def __init__(self, userName, roomID):
        # Server configuration
        self.HOST = '127.0.0.1'
        self.PORT = 12345

        # List to keep track of connected clients
        self.clients = []
        self.rooms = []
        self.messageHistory = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.server.listen(5)
        print(f"Server started on {self.HOST}:{self.PORT}")

        room = ChatRoom.ChatRoom(roomID, "Room 1")
        self.rooms.append(room)

        while True:
            client_socket, client_address = self.server.accept()

            if not self.rooms:
                client_socket.send("Would you like to create a room? Enter y or n:".encode('utf-8'))
            else:
                client_socket.send("Available Rooms: ".encode('utf-8'))
                for room_item in self.rooms:
                    client_socket.send(f"{room_item.roomNumber}".encode('utf-8'))

            client = dict(name=userName, room=room, socket=client_socket, address=client_address)
            self.clients.append(client)

            room.add_user(client)
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

    def handle_client(self, client):
        client_socket = client["socket"]
        room = client["room"]
        
        name = client["name"]
        print(f"{name}, {client['address']} has joined the chatroom")
        room.broadcast(f"{name} has joined the chatroom", client)
            
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    self.messageHistory.append(f"{name}: {message}")
                    room.broadcast(f"[{name}] {message}", client)
                else:
                    self.clients.remove(client)
                    room.remove_user(client)
                    break
            except Exception as e:
                self.clients.remove(client)
                room.remove_user(client)
                print(f"{name} has left the chatroom due to an error: {e}")
                break

    def receive_messages(self):
        buffer = self.messageHistory
        self.messageHistory = []
        return buffer