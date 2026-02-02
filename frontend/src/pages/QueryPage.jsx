import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import QueryBox from "../components/QueryBox";
import AnswerBox from "../components/AnswerBox";
import { getActiveVersion } from "../api/queryApi";

export default function QueryPage() {
  const [activeVersion, setActiveVersion] = useState("");
  const [response, setResponse] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    getActiveVersion().then(v => setActiveVersion(v.active_version));
  }, []);

  return (
    <div style={{ padding: 30 }}>
      <h2>❓ Ask Question</h2>
      <p><b>Active Knowledge Version:</b> {activeVersion}</p>

      <QueryBox onAnswer={setResponse} />
      {response && <AnswerBox response={response} />}

      <br />
      <button onClick={() => navigate("/")}>
        ← Back to Knowledge Management
      </button>
    </div>
  );
}
