import { useState } from "react";

export default function QueryBox({ onAsk }) {
  const [question, setQuestion] = useState("");

  const submit = e => {
    e.preventDefault();
    onAsk(question);
  };

  return (
    <form onSubmit={submit}>
      <input
        value={question}
        onChange={e => setQuestion(e.target.value)}
        placeholder="Ask something..."
      />
      <button type="submit">Ask</button>
    </form>
  );
}
