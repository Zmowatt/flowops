import { useEffect, useState } from "react";
import RequestCard from "../components/RequestCard";

function Dashboard() {
    const [requests, setRequests] = useState([]);

    useEffect(() => {
        fetch("http://localhost:5555/requests", {
            credentials: "include",
        })
            .then((res) => res.json())
            .then(setRequests);
    }, []);

    return (
        <div>
            <h1>FlowOps Dashboard</h1>

            {requests.map((request) => (
                <RequestCard key={request.id} request={request} />
            ))}
        </div>
    );
}

export default Dashboard;