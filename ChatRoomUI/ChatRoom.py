class ChatRoom:
    def __init__(self, roomNumber, roomName):
        self.users = []
        self.roomNumber = roomNumber
        self.roomName = roomName

    def add_user(self, user):
        self.users.append(user)
        print(f"Connection from {user['address']}")

    def remove_user(self, user):
        user["socket"].close()
        print(f"{user['name']} has left the chatroom")
        self.broadcast(f"{user['name']} has left the chatroom", user)
        self.users.remove(user)

    def remove_all_users(self):
        for user in self.users:
            user["socket"].close()
        self.users = []

    def broadcast(self, message, sender_client):
        for user in self.users:
            if user != sender_client:
                try:
                    user["socket"].send(message.encode('utf-8'))
                except:
                    user["socket"].close()
                    self.users.remove(user)