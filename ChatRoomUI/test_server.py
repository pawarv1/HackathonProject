import socket
import threading
import server
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/startServer', methods=['POST'])
def start_server():
    data = request.get_json()
    name = data.get("name")
    room_id = data.get("roomID")

    server = server.startServer(name, room_id)

    if not name or not room_id:
        return jsonify({"message": "Name and Room ID are required!"}), 400

    return jsonify({"message": f"Server started for {name} in room {room_id}!"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)