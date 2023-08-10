import React, { useState } from "react";
import del from "../assets/delete.png";

const MessageHistory = ({
  messages,
  handleDeleteMessage,
  handleNewChatClick,
}) => {
  const filteredMessages = messages.filter(
    (message) => message.sender !== "bot"
  );

  return (
    <div className="message-history">
      <div className="side-menu-button" onClick={handleNewChatClick}>
        <span>+</span>New Chat
      </div>
      <div style={{ margin: "40px 0px" }}>
        {" "}
        {filteredMessages.map((message) => (
          <div key={message.id} className="message">
            <span className="msg-span">{message.text}</span>
            <span
              className="delete-icon"
              onClick={() => handleDeleteMessage(message.id)}
            >
              <img src={del} style={{ width: "20px" }}></img>
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MessageHistory;
