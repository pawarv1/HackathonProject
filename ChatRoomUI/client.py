import socket
import threading

class Client:
    def __init__(self, userName, roomID):
        # Server configuration
        self.HOST = '127.0.0.1'
        self.PORT = 12345

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))

        self.userName = userName
        self.roomID = roomID

        thread = threading.Thread(target=self.receive_messages)
        thread.start()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    print(message)
                else:
                    self.client_socket.close()
                    break
            except:
                self.client_socket.close()
                break

    def send_message(self, message):
        print(f"Sending message: {message}")
        if not message:
            self.client_socket.close()
        self.client_socket.send(message.encode('utf-8'))