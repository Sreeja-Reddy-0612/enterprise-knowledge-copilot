import { useState } from "react";
import { rollbackVersion, getActiveVersion } from "../api/queryApi";

export default function RollbackBox({ setActiveVersion }) {
  const [version, setVersion] = useState("");

  const rollback = async () => {
    if (!version) return;
    await rollbackVersion(version);
    const active = await getActiveVersion();
    setActiveVersion(active);
  };

  return (
    <>
      <input
        placeholder="Version to rollback"
        value={version}
        onChange={e => setVersion(e.target.value)}
      />
      <button onClick={rollback}>Rollback</button>
    </>
  );
}
