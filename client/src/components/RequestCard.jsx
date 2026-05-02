import { Link } from "react-router-dom"

function RequestCard({ request }) {
    return(
        <div>
            <h3>{request.job_name}</h3>
            <p>{request.address}</p>
            <p>Parts: {request.parts_requested}</p>
            <p>Status: {request.status}</p>
            <p>Priority: {request.priority}</p>
            <Link to={` /request/${request.id}`}>View Details</Link>
            <hr />
        </div>
    );
}

export default RequestCard;