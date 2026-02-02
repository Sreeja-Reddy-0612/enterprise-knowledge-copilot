import { useState } from "react";
import { ingestDoc } from "../api/queryApi";

export default function UploadBox({ onDone }) {
  const [file, setFile] = useState(null);
  const [version, setVersion] = useState("");

  async function handleUpload() {
    await ingestDoc(file, version);
    alert("Document ingested");
    onDone();
  }

  return (
    <div>
      <h3>📤 Upload Knowledge</h3>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <input
        placeholder="Knowledge Version"
        value={version}
        onChange={e => setVersion(e.target.value)}
      />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}
