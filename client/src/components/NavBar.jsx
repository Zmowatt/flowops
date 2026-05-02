import { Link } from "react-router-dom";

function NavBar({ setCurrentUser }) {
  function handleLogout() {
    fetch("http://localhost:5555/logout", {
      method: "DELETE",
      credentials: "include",
    }).then(() => setCurrentUser(null));
  }

  return (
    <nav>
      <Link to="/">Dashboard</Link>{" | "}
      <Link to="/requests/new">New Request</Link>{" | "}
      <button onClick={handleLogout}>Logout</button>
    </nav>
  );
}

export default NavBar;