export default function AnswerBox({ response }) {
  if (!response) return null;

  return (
    <>
      <h3>Answer</h3>
      <p>{response.answer}</p>
      <p><b>Version:</b> {response.knowledge_versions?.join(", ")}</p>
      <p><b>Trace ID:</b> {response.trace_id}</p>
    </>
  );
}
