import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import UploadBox from "../components/UploadBox";
import RollbackBox from "../components/RollbackBox";
import { getActiveVersion } from "../api/queryApi";

export default function HomePage() {
  const [activeVersion, setActiveVersion] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    getActiveVersion().then(v => setActiveVersion(v.active_version));
  }, []);

  return (
    <div style={{ padding: 30 }}>
      <h1>🧠 Enterprise Knowledge Co-Pilot</h1>

      <p><b>Active Knowledge Version:</b> {activeVersion}</p>

      <UploadBox onDone={() => window.location.reload()} />
      <RollbackBox onDone={() => window.location.reload()} />

      <br />
      <button onClick={() => navigate("/query")}>
        Ask Questions →
      </button>
    </div>
  );
}
