import "./App.css";
import MainDashboard from "./components/MainDashboard";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./components/Home";

const App = () => {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<Home />}></Route>
          <Route
            exact
            path="/chat-dashboard"
            element={<MainDashboard />}
          ></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
};
export default App;
