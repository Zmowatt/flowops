import { useState } from "react";
import { useNavigate } from "react-router-dom";

function NewRequest() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    job_name: "",
    address: "",
    parts_requested: "",
    date_needed: "",
    priority: "Normal",
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

    fetch("http://localhost:5555/requests", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify(formData),
    }).then((res) => {
      if (res.ok) {
        navigate("/");
      } else {
        res.json().then((data) => {
          setError(data.error || "Something went wrong");
        });
      }
    });
  }

  return (
    <div>
      <h1>New Request</h1>

      <form onSubmit={handleSubmit}>
        <input
          name="job_name"
          value={formData.job_name}
          onChange={handleChange}
          placeholder="Job Name"
        />

        <input
          name="address"
          value={formData.address}
          onChange={handleChange}
          placeholder="Address"
        />

        <textarea
          name="parts_requested"
          value={formData.parts_requested}
          onChange={handleChange}
          placeholder="Parts Requested"
        />

        <input
          name="date_needed"
          type="date"
          value={formData.date_needed}
          onChange={handleChange}
        />

        <select
          name="priority"
          value={formData.priority}
          onChange={handleChange}
        >
          <option value="Low">Low</option>
          <option value="Normal">Normal</option>
          <option value="Urgent">Urgent</option>
        </select>

        <button type="submit">Create Request</button>
      </form>

      {error && <p>{error}</p>}
    </div>
  );
}

export default NewRequest;
