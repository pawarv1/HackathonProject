import server
import client
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

serverObj = None
clientList = []

# Server intialization
@app.route('/startServer', methods=['POST'])
def start_server():
    
    data = request.get_json()
    userName = data.get("userName")
    roomID = data.get("roomID")

    if not userName or not roomID:
        return jsonify({"message": "User Name and Room ID are required!"}), 400
    else:
        serverObj = server.Server(userName, roomID)
    
    #return jsonify({"message": f"Server started for {userName} in room id {roomID}!"})


# Client initialization
@app.route('/startClient', methods=['POST'])
def start_client():
    data = request.get_json()
    userName = data.get("userName")
    roomID = data.get("roomID")

    newClient = client.Client(userName, roomID)
    newClient.send_message("Hello from client!")
    clientList.append(newClient)

    if not userName or not roomID:
        return jsonify({"message": "User Name and Room ID are required!"}), 400

    return jsonify({"message": f"User {userName} is attempting to connect to room id {roomID}"})

def receive_messages():
    return serverObj.receive_messages()

if __name__ == "__main__":
    app.run(debug=True, port=5000)