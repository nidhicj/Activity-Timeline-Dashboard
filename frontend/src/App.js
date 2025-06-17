import { useState } from "react";
import axios from "axios";

function App() {
  const [quote, setQuote] = useState("");

  const fetchQuote = async () => {
    const response = await axios.get("http://localhost:8000/quote");
    console.log(response);
    setQuote(response.data.quote);
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "50vh" }}
       className="App">
      <h1>Quote Generator</h1>
      <button onClick={fetchQuote}>Get Quote</button>
      <p>{quote}</p>
    </div>
  );
}

export default App;
