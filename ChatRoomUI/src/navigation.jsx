import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Server from './pages/Server';
import Client from './pages/Client';

function Navigation() {
    return (
        <>
            <Router>
                <nav>
                    <button id = "HomeButton">
                        <Link to="/">Home</Link>
                    </button>
                    <button id = "CreateRoomButton">
                        <Link to="/server">Create a new room</Link>
                    </button>
                    <button id = "JoinRoomButton">
                        <Link to="/client">Join a room</Link>
                    </button>
                </nav>
                <main>
                    <Routes>
                        <Route path="/" element={<Home></Home>} />
                        <Route path="/server" element={<Server></Server>} />
                        <Route path="/client" element={<Client></Client>} />
                    </Routes>
                </main>
            </Router>
        </>
    );
}

export default Navigation;