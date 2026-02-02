import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import QueryPage from "./pages/QueryPage";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/query" element={<QueryPage />} />
      </Routes>
    </BrowserRouter>
  );
}
