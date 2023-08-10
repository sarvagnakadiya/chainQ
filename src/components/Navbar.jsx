import React, { useState } from "react";
import { Link } from "react-router-dom";
import ConnectButtonCustom from "./Connectbuttoncustom";
import "../style/ConnectButtonCustom.scss";
import logo from "../assets/logo.png";

function Navbar() {
  const [isExpanded, setIsExpanded] = useState(false);
  const [address, setAddress] = useState("");

  function handleClick() {
    setIsExpanded(!isExpanded);
  }
  return (
    <>
      <header className="header">
        <nav className="navbar">
          <span className="logo" style={{ width: "30%" }}>
            <Link to="/">
              <img src={logo} alt="logo" style={{ width: "30%" }} />
            </Link>
          </span>
          <div style={{ width: "30%" }}>
            <ConnectButtonCustom />
          </div>
        </nav>
      </header>
    </>
  );
}

export default Navbar;
