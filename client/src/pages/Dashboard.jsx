import { useEffect, useEffectEvent, useState } from "react";
import RequestCard from "../components/RequestCards";
import { requestFormReset } from "react-dom";

function Dashboard() {
    const [reqests, setRequests] = useState([]);

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

            {request.map((request) => (
                <RequestCard key={request.id} request={request} />
            ))}
        </div>
    );
}

export default Dashboard;