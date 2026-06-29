import { useState, useRef, useEffect } from "react";
import "./App.css";

const API_URL = "https://jana-ai-api.onrender.com/chat";

export default function App() {
  const [messages, setMessages] = useState([
    { role: "bot", text: "Hi Jana! I'm Pixel. Ask me anything." },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const endRef = useRef(null);

  // Auto-scroll to the newest message whenever messages change
  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  async function sendMessage() {
    const text = input.trim();
    if (!text || loading) return;

    setMessages((prev) => [...prev, { role: "user", text }]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });
      if (!res.ok) throw new Error("Server error " + res.status);
      const data = await res.json();
      setMessages((prev) => [...prev, { role: "bot", text: data.reply }]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "error", text: "⚠️ Couldn't reach the API. Is the server running?" },
      ]);
    } finally {
      setLoading(false);
    }
  }

  function handleKeyDown(e) {
    if (e.key === "Enter") sendMessage();
  }

  return (
    <div className="app">
      <div className="chat">
        <div className="header">🤖 Pixel</div>

        <div className="messages">
          {messages.map((m, i) => (
            <div key={i} className={`msg ${m.role}`}>
              {m.text}
            </div>
          ))}
          {loading && <div className="msg bot typing">…</div>}
          <div ref={endRef} />
        </div>

        <div className="input-row">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type a message..."
            autoComplete="off"
          />
          <button onClick={sendMessage} disabled={loading}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
}