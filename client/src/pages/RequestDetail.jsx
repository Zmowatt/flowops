import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

function RequestDetail() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [request, setRequest] = useState(null);
  const [updates, setUpdates] = useState([]);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(`http://localhost:5555/requests/${id}`, {
      credentials: "include",
    })
      .then((res) => res.json())
      .then(setRequest);

    fetch(`http://localhost:5555/requests/${id}/updates`, {
      credentials: "include",
    })
      .then((res) => res.json())
      .then(setUpdates);
  }, [id]);

  function handleStatusChange(e) {
    const newStatus = e.target.value;

    fetch(`http://localhost:5555/requests/${id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ status: newStatus }),
    }).then((res) => {
      if (res.ok) {
        res.json().then(setRequest);
      } else {
        res.json().then((data) => setError(data.error));
      }
    });
  }

  function handleDelete() {
    fetch(`http://localhost:5555/requests/${id}`, {
      method: "DELETE",
      credentials: "include",
    }).then((res) => {
      if (res.ok) {
        navigate("/");
      } else {
        res.json().then((data) => setError(data.error));
      }
    });
  }

  function handleAddUpdate(e) {
    e.preventDefault();

    fetch(`http://localhost:5555/requests/${id}/updates`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ message }),
    }).then((res) => {
      if (res.ok) {
        res.json().then((newUpdate) => {
          setUpdates([...updates, newUpdate]);
          setMessage("");
        });
      } else {
        res.json().then((data) => setError(data.error));
      }
    });
  }

  if (!request) return <p>Loading...</p>;

  return (
    <div>
      <h1>{request.job_name}</h1>

      {error && <p>{error}</p>}

      <p><strong>Address:</strong> {request.address}</p>
      <p><strong>Parts:</strong> {request.parts_requested}</p>
      <p><strong>Date Needed:</strong> {request.date_needed}</p>
      <p><strong>Priority:</strong> {request.priority}</p>

      <label>
        <strong>Status:</strong>{" "}
        <select value={request.status} onChange={handleStatusChange}>
          <option value="Requested">Requested</option>
          <option value="In Progress">In Progress</option>
          <option value="Ready">Ready</option>
          <option value="Completed">Completed</option>
        </select>
      </label>

      <br />
      <br />

      <button onClick={handleDelete}>Delete Request</button>

      <hr />

      <h2>Updates</h2>

      <form onSubmit={handleAddUpdate}>
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Add an update"
        />
        <button type="submit">Add Update</button>
      </form>

      {updates.map((update) => (
        <div key={update.id}>
          <p>{update.message}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default RequestDetail;