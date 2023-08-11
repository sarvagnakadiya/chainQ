import React, { useState, useEffect } from "react";
import { v4 as uuidv4 } from "uuid";
import "../style/main.scss";
import EmptyComponent from "./EmptyComponent";
import ChatLog from "./ChatLog";
import MessageHistory from "./MessageHistory";
import send from "../assets/send.png";
import axios from "axios";

const Dashboard = () => {
  const [newMessage, setNewMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [showChatLog, setShowChatLog] = useState(false);

  useEffect(() => {
    if (
      messages.length > 0 &&
      messages[messages.length - 1].sender === "user"
    ) {
      setShowChatLog(true);
    }
  }, [messages]);

  const sendMessage = () => {
    if (newMessage.trim() !== "") {
      const userMessage = {
        id: uuidv4(),
        sender: "user",
        text: newMessage,
      };
      setMessages((prevMessages) => [...prevMessages, userMessage]);
      setNewMessage("");

      const requestData = {
        user_prompt: newMessage,
      };

      axios
        .post("http://173.82.54.146:5001/get_answer", requestData, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          const botResponse = {
            id: uuidv4(),
            sender: "bot",
            text: response.data.answer,
          };
          setMessages((prevMessages) => [...prevMessages, botResponse]);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  };

  // const simulateBotResponse = () => {
  //   setTimeout(() => {
  //     const botMessage = {
  //       id: uuidv4(),
  //       sender: "bot",
  //       text: "I'm just a bot response.",
  //     };
  //     setMessages((prevMessages) => [...prevMessages, botMessage]);
  //   }, 1000);
  // };

  const handleDeleteMessage = (messageId) => {
    const messageIndex = messages.findIndex(
      (message) => message.id === messageId
    );
    if (messageIndex === -1) {
      return;
    }
    const isUserMessage = messages[messageIndex].sender === "user";
    setMessages((prevMessages) => {
      const updatedMessages = [...prevMessages];
      updatedMessages.splice(messageIndex, 1);
      if (
        isUserMessage &&
        messageIndex < updatedMessages.length &&
        updatedMessages[messageIndex].sender === "bot"
      ) {
        updatedMessages.splice(messageIndex, 1);
      }
      return updatedMessages;
    });
  };

  const handleNewChatClick = () => {
    setShowChatLog(false);
  };

  const isSendButtonDisabled = newMessage === "";

  const handleKeyPress = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      sendMessage();
    }
  };

  const userPrompt = "Your user prompt here";
  const requestData = { user_prompt: userPrompt };

  return (
    <div className="chat-app-container">
      <MessageHistory
        messages={messages}
        handleDeleteMessage={handleDeleteMessage}
        handleNewChatClick={handleNewChatClick}
      />

      <div className="chat-box-main">
        <div className="chat-box">
          {messages.length === 0 || !showChatLog ? (
            <EmptyComponent />
          ) : (
            <>
              <ChatLog messages={messages} />
            </>
          )}
          <div className="chat-input">
            <input
              type="text"
              value={newMessage}
              onChange={(e) => setNewMessage(e.target.value)}
              onKeyDown={handleKeyPress}
              placeholder="Type your message..."
            />
            <button
              onClick={sendMessage}
              disabled={isSendButtonDisabled}
              className="send-btn"
            >
              <img src={send} style={{ width: "20px" }}></img>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
