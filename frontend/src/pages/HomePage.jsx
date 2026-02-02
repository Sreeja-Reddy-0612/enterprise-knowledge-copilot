import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  getActiveVersion,
  uploadKnowledge,
  rollbackVersion,
} from "../api/queryApi";

export default function HomePage() {
  const [activeVersion, setActiveVersion] = useState("");
  const [file, setFile] = useState(null);
  const [version, setVersion] = useState("");
  const [rollback, setRollback] = useState("");

  const navigate = useNavigate();

  useEffect(() => {
    loadActiveVersion();
  }, []);

  async function loadActiveVersion() {
    const data = await getActiveVersion();
    setActiveVersion(data.active_version || "None");
  }

  async function handleUpload() {
    if (!file || !version) {
      alert("File and version required");
      return;
    }
    await uploadKnowledge(file, version);
    alert(`Uploaded & activated version: ${version}`);
    setVersion("");
    loadActiveVersion();
  }

  async function handleRollback() {
    if (!rollback) {
      alert("Enter version to rollback");
      return;
    }
    await rollbackVersion(rollback);
    alert(`Rolled back to version: ${rollback}`);
    setRollback("");
    loadActiveVersion();
  }

  return (
    <div>
      <h1>🧠 Enterprise Knowledge Co-Pilot</h1>

      <p>
        <b>Active Knowledge Version:</b>{" "}
        <span style={{ color: "green" }}>{activeVersion}</span>
      </p>

      <hr />

      <h3>📤 Upload Knowledge</h3>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <br />
      <input
        placeholder="Knowledge Version"
        value={version}
        onChange={(e) => setVersion(e.target.value)}
      />
      <button onClick={handleUpload}>Upload</button>

      <hr />

      <h3>⏪ Rollback Version</h3>
      <input
        placeholder="Version to rollback"
        value={rollback}
        onChange={(e) => setRollback(e.target.value)}
      />
      <button onClick={handleRollback}>Rollback</button>

      <hr />

      <button onClick={() => navigate("/query")}>
        Ask Questions →
      </button>
    </div>
  );
}
