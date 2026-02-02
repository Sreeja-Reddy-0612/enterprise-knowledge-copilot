export default function AnswerBox({ response }) {
  return (
    <div style={{ marginTop: 20 }}>
      <h3>✅ Answer</h3>
      <p>{response.answer}</p>

      <p><b>Knowledge Versions:</b> {response.knowledge_versions?.join(", ")}</p>
      <p><b>Trace ID:</b> {response.trace_id}</p>
    </div>
  );
}
