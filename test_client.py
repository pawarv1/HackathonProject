import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# Flag to stop the thread
stop_thread = False

def receive_messages(client_socket):
    global stop_thread
    while not stop_thread:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print("Msg from user: " + message)
            else:
                client_socket.close()
                break
        except:
            client_socket.close()
            break

def main():
    global stop_thread
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("\n*** Welcome to the chat room. Enter a blank msg to exit ***")

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input()
        if not message:
            stop_thread = True
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()