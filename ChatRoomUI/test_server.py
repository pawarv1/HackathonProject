import socket
import threading
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/startServer', methods=['POST'])
def start_server():
    data = request.get_json()
    userName = data.get("userName")
    roomName = data.get("roomName")

    if not userName or not roomName:
        return jsonify({"message": "User Name and Room Name are required!"}), 400

    return jsonify({"message": f"Server started for {userName} in room {roomName}!"})

@app.route('/startClient', methods=['POST'])
def start_client():
    data = request.get_json()
    roomName = data.get("roomName")
    roomID = data.get("roomID")

    if not roomName or not roomID:
        return jsonify({"message": "Room Name and Room ID are required!"}), 400

    return jsonify({"message": f"Attempting to connect to {roomName} and room id {roomID}"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)