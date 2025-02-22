import { useState } from "react";

    function Server() {
        const [name, setName] = useState("");
        const [roomID, setRoomID] = useState("");

        const handleSubmit = async (event) => {
            event.preventDefault(); // Prevent page reload

            const response = await fetch("http://127.0.0.1:5000/startServer", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name, roomID }),
            });

        const data = await response.json();
        alert(data.message); // Display server response
    };


    return (
        <div>
            <h1>Welcome to Server</h1>
            <form onSubmit={handleSubmit}>
                <label for="Name">Enter your name:</label>
                <input type="text" id="Name" value={name} onChange={(e) => setName(e.target.value)}></input><br></br>
                <label for="roomID">Enter your room id:</label>
                <input type="text" id="roomID" value={roomID} onChange={(e) => setRoomID(e.target.value)}></input><br></br>
                <button type="submit">Create Room</button>
            </form>
        </div>
    );
}

export default Server;