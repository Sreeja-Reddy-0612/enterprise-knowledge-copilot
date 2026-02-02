const BASE_URL = "http://127.0.0.1:8001";

export async function getActiveVersion() {
  const res = await fetch(`${BASE_URL}/version/active`);
  return res.json();
}

export async function uploadKnowledge(file, version) {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("knowledge_version", version);

  const res = await fetch(`${BASE_URL}/ingest`, {
    method: "POST",
    body: formData,
  });

  return res.json();
}

export async function rollbackVersion(version) {
  const res = await fetch(`${BASE_URL}/version/rollback`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ version }),
  });

  return res.json();
}

export async function askQuestion(question) {
  const res = await fetch(`${BASE_URL}/query`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });

  return res.json();
}
