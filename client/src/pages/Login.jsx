import { useState } from "react";

function Login({ setCurrentUser }) {
  const [email, setEmail] = useState("zmowatt@company.com");
  const [password, setPassword] = useState("password123");
  const [error, setError] = useState("");

  function handleSubmit(e) {
    e.preventDefault();

    fetch("http://localhost:5555/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ email, password }),
    }).then((res) => {
      if (res.ok) {
        res.json().then(setCurrentUser);
      } else {
        res.json().then((data) => setError(data.error));
      }
    });
  }

  return (
    <div>
      <h1>FlowOps Login</h1>

      <form onSubmit={handleSubmit}>
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
        />

        <input
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
          type="password"
        />

        <button type="submit">Log In</button>
      </form>

      {error && <p>{error}</p>}
    </div>
  );
}

export default Login;