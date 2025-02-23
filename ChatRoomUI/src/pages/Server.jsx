import { useState } from "react";

    function Server() {
        const [userName, setUserName] = useState("");
        const [roomName, setRoomName] = useState("");

        const handleSubmit = async (event) => {
            event.preventDefault(); // Prevent page reload

            const response = await fetch("http://127.0.0.1:5000/startServer", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ userName, roomName }),
            });

        const data = await response.json();
        alert(data.message); // Display server response
    };


    return (
        <div>
            <h1>Welcome to Server</h1>
            <form onSubmit={handleSubmit}>
                <label for="userName">Enter your username:</label>
                <input type="text" id="userName" value={userName} onChange={(e) => setUserName(e.target.value)}></input><br></br>
                <label for="roomName">Enter your room name:</label>
                <input type="text" id="roomName" value={roomName} onChange={(e) => setRoomName(e.target.value)}></input><br></br>
                <button type="submit">Create Room</button>
            </form>
        </div>
    );
}

export default Server;