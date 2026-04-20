import { useState } from "react";

function App() {
  const [problem, setProblem] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const solveBug = async () => {
    setLoading(true);
    setResult(null);

    try {
      const res = await fetch("http://127.0.0.1:8000/solve", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ problem }),
      });

      const data = await res.json();
      setResult(data);
    } catch (error) {
      setResult({
        result: "Error: Backend not reachable or API failed.",
      });
    }

    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: "50px auto", fontFamily: "Arial" }}>
      <h1 style={{ textAlign: "center" }}>🧠 AI Bug Assistant</h1>

      <textarea
        rows="5"
        style={{ width: "100%", padding: "10px" }}
        placeholder="Describe your bug..."
        value={problem}
        onChange={(e) => setProblem(e.target.value)}
      />

      <button
        onClick={solveBug}
        style={{
          width: "100%",
          padding: "10px",
          marginTop: "10px",
          background: "black",
          color: "white",
          cursor: "pointer",
        }}
      >
        {loading ? "Solving..." : "Solve Bug"}
      </button>

      {result && (
        <div style={{ marginTop: 20, padding: 15, border: "1px solid #ccc" }}>
          <h3>AI Response:</h3>

          <pre style={{ whiteSpace: "pre-wrap" }}>
            {result.result}
          </pre>
        </div>
      )}
    </div>
  );
}

export default App;