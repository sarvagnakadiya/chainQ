// import React, { useState } from "react";
// import del from "../assets/delete.png";
// import cov from "../assets/covalent-logo.jpg";
// import rightUp from "../assets/right-up.png";

// const MessageHistory = ({
//   messages,
//   handleDeleteMessage,
//   handleNewChatClick,
// }) => {
//   const filteredMessages = messages.filter(
//     (message) => message.sender !== "bot"
//   );

//   return (
//     <>
//       <div className="message-history">
//         <div className="side-menu-button" onClick={handleNewChatClick}>
//           <span>+</span>New Chat
//         </div>
//         <div className="chat-history-list" style={{ margin: "40px 0px" }}>
//           {" "}
//           {filteredMessages.map((message) => (
//             <div key={message.id} className="message">
//               <span className="msg-span">{message.text}</span>
//               <span
//                 className="delete-icon"
//                 onClick={() => handleDeleteMessage(message.id)}
//               >
//                 <img src={del} style={{ width: "20px" }}></img>
//               </span>
//             </div>
//           ))}
//         </div>
//         <div className="exp-cov-class-main">
//           <div className="side-ex-cov-btn">
//             <img
//               src={cov}
//               alt="cov-logo"
//               style={{ width: "20px", marginLeft: "5px", marginTop: "3px" }}
//             />
//             Explore Covalent
//             <img
//               src={rightUp}
//               alt=""
//               style={{ width: "13px", marginLeft: "60px", right: 0 }}
//             />
//           </div>
//         </div>
//       </div>
//     </>
//   );
// };

// export default MessageHistory;

import React, { useState } from "react";
import del from "../assets/delete.png";
import cov from "../assets/covalent-logo.jpg";
import rightUp from "../assets/right-up.png";

const MessageHistory = ({
  messages,
  handleDeleteMessage,
  handleNewChatClick,
}) => {
  const filteredMessages = messages.filter(
    (message) => message.sender !== "bot"
  );

  return (
    <>
      <div className="message-history">
        <div className="side-menu-button" onClick={handleNewChatClick}>
          <span>+</span>New Chat
        </div>
        <div className="chat-history-list" style={{ margin: "40px 0px" }}>
          {filteredMessages.length === 0 ? (
              <div className="no-messages-center" style={{ color: "white" }}>
                No prompts yet.
              </div>
          ) : (
            filteredMessages.map((message) => (
              <div key={message.id} className="message">
                <span className="msg-span">{message.text}</span>
                <span
                  className="delete-icon"
                  onClick={() => handleDeleteMessage(message.id)}
                >
                  <img src={del} style={{ width: "20px" }} alt="Delete" />
                </span>
              </div>
            ))
          )}
        </div>
        <div className="exp-cov-class-main">
          <div className="side-ex-cov-btn">
            <img
              src={cov}
              alt="cov-logo"
              style={{ width: "20px", marginLeft: "5px", marginTop: "3px" }}
            />
            Explore Covalent
            <img
              src={rightUp}
              alt=""
              style={{ width: "13px", marginLeft: "60px", right: 0 }}
            />
          </div>
        </div>
      </div>
    </>
  );
};

export default MessageHistory;
