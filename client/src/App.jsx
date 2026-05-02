import { useEffect, useState } from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Dashboard from "./pages/Dashboard";
import NewRequest from "./pages/NewRequest";
import RequestDetail from "./pages/RequestDetail";
import NavBar from "./components/NavBar";

function App() {
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5555/check_session", {
      credentials: "include",
    }).then((res) => {
      if (res.ok) {
        res.json().then(setCurrentUser);
      }
    });
  }, []);

  if (!currentUser) {
    return (
      <Routes>
        <Route path="/signup" element={<Signup setCurrentUser={setCurrentUser} />} />
        <Route path="*" element={<Login setCurrentUser={setCurrentUser} />} />
      </Routes>
    );
  }

  return (
    <>
      <NavBar setCurrentUser={setCurrentUser} />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/requests/new" element={<NewRequest />} />
        <Route path="/requests/:id" element={<RequestDetail />} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </>
  );
}

export default App;