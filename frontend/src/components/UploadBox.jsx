import { useState } from "react";
import { uploadKnowledge, getActiveVersion } from "../api/queryApi";

export default function UploadBox({ setActiveVersion }) {
  const [file, setFile] = useState(null);
  const [version, setVersion] = useState("");

  const upload = async () => {
    if (!file || !version) return;
    await uploadKnowledge(file, version);
    const active = await getActiveVersion();
    setActiveVersion(active);
  };

  return (
    <>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <input
        placeholder="Knowledge Version"
        value={version}
        onChange={e => setVersion(e.target.value)}
      />
      <button onClick={upload}>Upload</button>
    </>
  );
}
