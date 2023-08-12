import React, { useState } from "react";
import axios from "axios";
import "../style/main.scss";

function EmptyComponent() {
  const [balances, setBalances] = useState([]);
  const [walletAddress, setWalletAddress] = useState("");

  const fetchBalances = () => {
    const headers = {
      Authorization: "Bearer ckey_6702edeceef9404abb0bf0b6331",
    };

    axios
      .get(
        `https://api.covalenthq.com/v1/matic-mainnet/address/${walletAddress}/balances_nft/`,
        { headers }
      )
      .then((response) => {
        setBalances(response.data.data.items);
      })
      .catch((error) => {
        console.error("Error fetching balances:", error);
      });
  };

  return (
    <div style={{ width: "70%", margin: "0 auto" }}>
      <h1 className="dash-title">Let's Explore The Power Of AI</h1>
      <div className="common-que-flex">
        <div style={{ width: "40%", flexDirection: "column", display: "flex" }}>
          <div
            style={{
              border: "1px solid lightgray",
              padding: "20px",
              textAlign: "justify",
              borderRadius: "10px",
              boxShadow: "0 0 8px 0 rgba(0, 0, 0, 0.25)",
            }}
          >
            <input
              type="text"
              placeholder="Enter ETH Address"
              onChange={(e) => setWalletAddress(e.target.value)}
            />
            <button onClick={fetchBalances}>Fetch Balances</button>
            <table>
              <thead>
                <tr>
                  <th>Contract Name</th>
                  <th>Contract Symbol</th>
                  <th>Contract Address</th>
                  <th>Balance</th>
                  <th>Last Transferred At</th>
                </tr>
              </thead>
              <tbody>
                {balances.map((balance) => (
                  <tr key={balance.contract_address}>
                    <td>{balance.contract_name}</td>
                    <td>{balance.contract_ticker_symbol}</td>
                    <td>{balance.contract_address}</td>
                    <td>{balance.balance}</td>
                    <td>{balance.last_transfered_at}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          {/* Repeat similar structure for other paragraphs */}
        </div>
      </div>
    </div>
  );
}

export default EmptyComponent;
