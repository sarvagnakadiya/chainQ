import React from "react";
import "../style/main.scss";
import Navbar from "./Navbar";
import hero from "../assets/hero.png";
import arrow from "../assets/Arrow.png";

function Home() {
  return (
    <>
      <div className="main-div-landing">
        <Navbar />
        <div className="landing-flex">
          <div className="home-left-section">
            <h1 className="home-title ">
              The AI -Powered Blockchain Data Querying System
            </h1>

            <p className=" home-desc">
              "Unleashing the Power of NLP and AI to Seamlessly Access and
              Analyze Blockchain Data"
            </p>

            <button className="try-btn">Try it first!</button>
          </div>
          <div className="hero-right">
            <div className="hero-right-inside">
              <img
                className="hero-right-bg1"
                src={hero}
                alt="backgroundimage"
              />
            </div>
          </div>
        </div>

        <footer>
          <div className="footer-flex">
            <div style={{ color: "white", fontSize: "15px" }}>
              © 2023 ChainQ. All Rights Reserved.
            </div>
          </div>
        </footer>
      </div>
    </>
  );
}

export default Home;
