import { Link } from "react-router-dom"

function RequestCard({ request }) {
  return (
    <div className="request-card">
      <h3>{request.job_name}</h3>
      <p>{request.address}</p>
      <p><strong>Parts:</strong> {request.parts_requested}</p>
      <p><span className="status">{request.status}</span></p>
      <p className="priority">Priority: {request.priority}</p>
      <Link to={`/requests/${request.id}`}>View Details</Link>
    </div>
  );
}

export default RequestCard;