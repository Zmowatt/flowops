import { useState } from "react";

function Signup({ setCurrentUser }) {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    role: "Requester",
  });

  const [error, setError] = useState("");

  function handleChange(e) {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  }

  function handleSubmit(e) {
    e.preventDefault();
    setError("");

    fetch("http://localhost:5555/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify(formData),
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
      <h1>FlowOps Signup</h1>

      <form onSubmit={handleSubmit}>
        <input
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Name"
        />

        <input
          name="email"
          value={formData.email}
          onChange={handleChange}
          placeholder="Email"
        />

        <input
          name="password"
          value={formData.password}
          onChange={handleChange}
          placeholder="Password"
          type="password"
        />

        <select name="role" value={formData.role} onChange={handleChange}>
          <option value="Requester">Requester</option>
          <option value="Fulfillment">Fulfillment</option>
          <option value="Manager">Manager</option>
        </select>

        <button type="submit">Sign Up</button>
      </form>

      {error && <p>{error}</p>}
    </div>
  );
}

export default Signup;