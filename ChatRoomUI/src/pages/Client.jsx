import { useState } from "react";

function Client() {
  const [roomName, setRoomName] = useState("");
  const [roomID, setRoomID] = useState("");

  const handleSubmit = async (event) => {
      event.preventDefault(); // Prevent page reload

      const response = await fetch("http://127.0.0.1:5000/startClient", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ roomName, roomID }),
      });

    const data = await response.json();
    alert(data.message); // Display server response
  };
  
  return (
    <div>
      <h1>Welcome to Client</h1>
      <form onSubmit={handleSubmit}>
          <label for="roomName">Enter the name of the room you want to join:</label>
          <input type="text" id="roomName" value={roomName} onChange={(e) => setRoomName(e.target.value)}></input><br></br>
          <label for="roomID">Enter the room ID:</label>
          <input type="text" id="roomID" value={roomID} onChange={(e) => setRoomID(e.target.value)}></input><br></br>
          <button type="submit">Join Room</button>
      </form>
    </div>
  );
}

export default Client;