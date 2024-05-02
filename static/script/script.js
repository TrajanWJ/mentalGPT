
function sendMessage() {
   var userInput = document.getElementById("user-input-field").value;
   if (userInput.trim() !== "") {
      appendUserMessage(userInput);
      getBotResponse(userInput);
      document.getElementById("user-input-field").value = "";
   }

   var chatArea = document.getElementById("chat-container");
   chatArea.scrollTop = chatArea.scrollHeight;
}

function appendBotMessage(message) {
   deleteLastMessage();
   _appendBotMessage(message);
}

function appendUserMessage(message) {
   var chatArea = document.getElementById("chat-area");
   var userMessageElement = document.createElement("div");
   userMessageElement.className = "user-message";
   userMessageElement.textContent = "You: " + message;
   chatArea.appendChild(userMessageElement);
   _appendBotMessage("Loading... DO NOT TYPE OR NUTHING")
}


function _appendBotMessage(message) {
   var chatArea = document.getElementById("chat-area");
   var botMessageElement = document.createElement("div");
   botMessageElement.className = "bot-message";
   botMessageElement.textContent = message;
   chatArea.appendChild(botMessageElement);
}

function deleteLastMessage() {
   var chatArea = document.getElementById("chat-area");
   var lastMessage = chatArea.lastChild;
   if (lastMessage) {
     chatArea.removeChild(lastMessage);
   }
}


//does bot response
function getBotResponse(userInput) {
   $.ajax({
      type: "POST",
      url: "/get_bot_response",
      data: { user_input: userInput },
      success: function (response) {
         appendBotMessage(response);
      },
   });
}


function _updateHotlines(newHotlines) {
   const hotlinesElement = document.querySelector('#hotlines');

   // Get the first .hotline element within #hotlines
   const firstHotline = hotlinesElement.querySelector('.hotline');
   const [[name, phone]] = Object.entries(newHotlines);

   // Update the content of the first .hotline element
   firstHotline.querySelector('h3').textContent = name;
   firstHotline.querySelector('p').textContent = phone;

   // Get the second .hotline element within #hotlines
   const secondHotline = hotlinesElement.querySelector('.hotline:nth-child(2)');
   const [, [name2, phone2]] = Object.entries(newHotlines);

   // Update the content of the second .hotline element
   secondHotline.querySelector('h3').textContent = name2;
   secondHotline.querySelector('p').textContent = phone2;
}

function updateHotlines() {
   $.ajax({
      type: "POST",
      url: "/get_hotlines",
      success: function (response) {
         _updateHotlines(response);
      },
   });
}


//make enter work
function handleKeyPress(event) {
   if (event.keyCode === 13) { // Enter key code
     event.preventDefault();
     sendMessage();
     updateHotlines();
   }
 }
 
 document.addEventListener("DOMContentLoaded", function() {
   var userInputField = document.getElementById("user-input-field");
   userInputField.addEventListener("keypress", handleKeyPress);
   _appendBotMessage("Everything you tell me is completely safe and private, I am a robot so I promise I won't tell anyone, so talk as explicitly in as clear and direct language as you can. Introduce yourself, trauma dump, spill tea, tell me how you're feeling, or just chat with me. ")

 });



const hiddenElements = document.querySelector(".hidden");
hiddenElements.forEach((el) => observer.observe(el));


