import { useState } from "react";
import { askQuestion } from "../api/queryApi";

export default function QueryBox({ onAnswer }) {
  const [question, setQuestion] = useState("");

  async function handleAsk() {
    const res = await askQuestion(question);
    onAnswer(res);
  }

  return (
    <div>
      <input
        style={{ width: "60%" }}
        placeholder="Ask your question..."
        value={question}
        onChange={e => setQuestion(e.target.value)}
      />
      <button onClick={handleAsk}>Ask</button>
    </div>
  );
}
