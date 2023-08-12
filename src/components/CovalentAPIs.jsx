import React, { useState } from "react";
import axios from "axios";
import "../style/CovalentAPIs.css"; // Import the new CSS file

function NewComponent() {
  const [response, setResponse] = useState([]);
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
        setResponse(response.data.data.items);
      })
      .catch((error) => {
        console.error("Error fetching response:", error);
      });
  };

  return (
    <div className="container">
      <h1 className="dash-title">Let's Explore The Power Of AI</h1>
      <div className="form-container">
        <div className="form-box">
          <input
            type="text"
            className="input-field"
            placeholder="Enter ETH Address"
            onChange={(e) => setWalletAddress(e.target.value)}
          />
          <button className="fetch-button" onClick={fetchBalances}>
            Fetch Balances
          </button>
        </div>
        <table className="balance-table">
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
            {response.map((balance) => (
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
    </div>
  );
}

export default NewComponent;
