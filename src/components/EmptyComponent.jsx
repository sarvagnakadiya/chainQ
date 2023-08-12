import React from "react";
import "../style/main.scss";

function EmptyComponent() {
  return (
    <div style={{ width: "70%", margin: "0 auto" }}>
      <h1 className="dash-title">
        <div>
          Let's Explore <span style={{ color: "green" }}>ChainQ</span>
        </div>
      </h1>
      <div className="common-que-flex">
        <div style={{ width: "40%", flexDirection: "column", display: "flex" }}>
          Prompts example
          <p
            style={{
              border: "1px solid lightgray",
              padding: "10px",
              textAlign: "justify",
              borderRadius: "10px",
              boxShadow: "0 0 8px 0 rgba(0, 0, 0, 0.25)",
            }}
          >
            How many total transactions for block 108019738?
          </p>
          <p
            style={{
              border: "1px solid lightgray",
              padding: "10px",
              textAlign: "justify",
              borderRadius: "10px",
              boxShadow: "0 0 8px 0 rgba(0, 0, 0, 0.25)",
            }}
          >
            And list all the transaction hashes?
          </p>
          <p
            style={{
              border: "1px solid lightgray",
              padding: "10px",
              borderRadius: "10px",
              textAlign: "justify",
              boxShadow: "0 0 8px 0 rgba(0, 0, 0, 0.25)",
            }}
          >
            Can you give me more information about the same block?
          </p>
        </div>
        <div style={{ width: "40%", display: "flex", flexDirection: "column" }}>
          Features
          <p
            style={{
              border: "1px solid lightgray",
              padding: "10px",
              borderRadius: "10px",
              boxShadow: "0 0 8px 0 rgba(0, 0, 0, 0.25)",
              textAlign: "justify",
            }}
          >
            Works for Optimism Mainnet
          </p>
          <p
            style={{
              border: "1px solid lightgray",
              padding: "10px",
              textAlign: "justify",
              borderRadius: "10px",
              boxShadow: "0 0 8px 0 rgba(0, 0, 0, 0.25)",
            }}
          >
            Continious chat querying
          </p>
          <p
            style={{
              border: "1px solid lightgray",
              padding: "10px",
              textAlign: "justify",
              borderRadius: "10px",
              boxShadow: "0 0 8px 0 rgba(0, 0, 0, 0.25)",
            }}
          >
            Also support Covalent APIs
          </p>
        </div>
      </div>
    </div>
  );
}

export default EmptyComponent;
