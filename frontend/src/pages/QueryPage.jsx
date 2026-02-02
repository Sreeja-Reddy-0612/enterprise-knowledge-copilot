import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { askQuestion, getActiveVersion } from "../api/queryApi";

export default function QueryPage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState(null);
  const [activeVersion, setActiveVersion] = useState("");

  const navigate = useNavigate();

  useEffect(() => {
    fetchVersion();
  }, []);

  async function fetchVersion() {
    const data = await getActiveVersion();
    setActiveVersion(data.active_version || "None");
  }

  async function handleAsk() {
    const res = await askQuestion(question);
    setAnswer(res);
  }

  return (
    <div>
      <h2>❓ Ask Question</h2>

      <p>
        <b>Active Knowledge Version:</b>{" "}
        <span style={{ color: "green" }}>{activeVersion}</span>
      </p>

      <input
        style={{ width: "70%" }}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask something..."
      />
      <button onClick={handleAsk}>Ask</button>

      {answer && (
        <>
          <h3>✅ Answer</h3>
          <p>{answer.answer}</p>

          <p><b>Version:</b> {answer.version}</p>
          <p><b>Trace ID:</b> {answer.trace_id}</p>
        </>
      )}

      <br />
      <button onClick={() => navigate("/")}>
        ← Back to Knowledge Management
      </button>
    </div>
  );
}
