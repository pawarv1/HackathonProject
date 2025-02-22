import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                client_socket.close()
                break
        except:
            client_socket.close()
            break

def main():
    # Get the user name
    user_name = input("Welcome to the chat! Enter your username: ")
    if not user_name:
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    # Send the user name
    client_socket.send(user_name.encode('utf-8'))

    while True:
        message = input()
        if not message:
            thread.join()
            break
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()