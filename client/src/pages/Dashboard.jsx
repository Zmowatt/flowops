import { useEffect, useState } from "react";
import RequestCard from "../components/RequestCard";

function Dashboard() {
  const [requests, setRequests] = useState([]);
  const [page, setPage] = useState(1);
  const [pagination, setPagination] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:5555/requests?page=${page}&per_page=5`, {
      credentials: "include",
    })
      .then((res) => res.json())
      .then((data) => {
        setRequests(data.requests);
        setPagination(data);
      });
  }, [page]);

  return (
    <div className="page">
      <div className="page-header">
        <h1>FlowOps Dashboard</h1>
        <p>Track internal requests, statuses, and updates.</p>
      </div>

      <div className="request-grid">
        {requests.map((request) => (
          <RequestCard key={request.id} request={request} />
        ))}
      </div>

      {pagination && (
        <div className="pagination">
          <button
            onClick={() => setPage(page - 1)}
            disabled={!pagination.has_prev}
          >
            Previous
          </button>

          <span>
            Page {pagination.page} of {pagination.pages}
          </span>

          <button
            onClick={() => setPage(page + 1)}
            disabled={!pagination.has_next}
          >
            Next
          </button>
        </div>
      )}
    </div>
  );
}

export default Dashboard;