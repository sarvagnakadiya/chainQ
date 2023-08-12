// import React, { useState } from "react";
// import del from "../assets/delete.png";
// import cov from "../assets/covalent-logo.jpg";
// import rightUp from "../assets/right-up.png";
// import leftArrow from "../assets/left-arrow.png"

// const MessageHistory = ({
//   messages,
//   handleDeleteMessage,
//   handleNewChatClick,
//   toggleCovalentAPIs,
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
//           {filteredMessages.length === 0 ? (
//             <div className="no-messages-center" style={{ color: "white" }}>
//               No prompts yet.
//             </div>
//           ) : (
//             filteredMessages.map((message) => (
//               <div key={message.id} className="message">
//                 <span className="msg-span">{message.text}</span>
//                 <span
//                   className="delete-icon"
//                   onClick={() => handleDeleteMessage(message.id)}
//                 >
//                   <img src={del} style={{ width: "20px" }} alt="Delete" />
//                 </span>
//               </div>
//             ))
//           )}
//         </div>
//         <div className="exp-cov-class-main" onClick={toggleCovalentAPIs}>
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

import React, { useState, useEffect } from "react";
import del from "../assets/delete.png";
import cov from "../assets/covalent-logo.jpg";
import rightUp from "../assets/right-up.png";
import leftArrow from "../assets/left-arrow.png";

const MessageHistory = ({
  messages,
  handleDeleteMessage,
  handleNewChatClick,
  toggleCovalentAPIs,
  showCovalentAPIs,
  covalentAPIsActive,
}) => {
  const [exploreText, setExploreText] = useState("Explore Covalent");
  const [exploreImage, setExploreImage] = useState(rightUp);

  useEffect(() => {
    if (covalentAPIsActive) {
      setExploreText("Back to prompt");
      setExploreImage(leftArrow);
    } else {
      setExploreText("Explore Covalent");
      setExploreImage(rightUp);
    }
  }, [showCovalentAPIs, covalentAPIsActive]);

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
        <div className="exp-cov-class-main" onClick={toggleCovalentAPIs}>
          <div className="side-ex-cov-btn">
            {!covalentAPIsActive && (
              <img
                src={cov}
                alt="cov-logo"
                style={{ width: "20px", marginLeft: "5px", marginTop: "3px" }}
              />
            )}
            {exploreText}
            <img
              src={exploreImage}
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
