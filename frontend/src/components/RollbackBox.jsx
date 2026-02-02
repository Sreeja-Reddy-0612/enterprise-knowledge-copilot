import { useState } from "react";
import { rollbackVersion } from "../api/queryApi";

export default function RollbackBox({ onDone }) {
  const [version, setVersion] = useState("");

  async function handleRollback() {
    await rollbackVersion(version);
    alert("Rollback completed");
    onDone();
  }

  return (
    <div>
      <h3>⏪ Rollback Version</h3>
      <input
        placeholder="Version to rollback"
        value={version}
        onChange={e => setVersion(e.target.value)}
      />
      <button onClick={handleRollback}>Rollback</button>
    </div>
  );
}
