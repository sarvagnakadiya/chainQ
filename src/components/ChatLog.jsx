import React from "react";

const ChatLog = ({ messages }) => {
  return (
    <div className="chat-log-main">
      <h1 className="chat-log-title">ChainQ</h1>
      <div className="chat-log">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`chat-msg-${
              message.sender === "user" ? "log" : "response"
            }`}
          >
            <div className="chat-msg-center">
              <div
                className={`chat-avatar-${
                  message.sender === "user" ? "user" : "response"
                }`}
              >
                {message.sender === "user" ? (
                  /* User avatar image */
                  <img
                    src="./profile.jpg"
                    alt="User Avatar"
                    style={{ width: "30px" }}
                  />
                ) : (
                  /* Bot avatar image */
                  <img
                    src="./AI.png"
                    alt="Bot Avatar"
                    style={{ width: "30px" }}
                  />
                )}
              </div>
              <div className="chat-msg">{message.text}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ChatLog;
