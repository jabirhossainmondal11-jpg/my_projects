const nameInput = document.getElementById("nameInput");
const greenBtn = document.getElementById("greenBtn");
const welcomeMsg = document.getElementById("welcomeMsg");

// Ekta function banalam jeta message update korbe
function showWelcomeMessage() {
    let userName = nameInput.value;
    
    if (userName === "") {
        welcomeMsg.innerText = "Age nam toh likho!";
        welcomeMsg.style.color = "red";
    } else {
        welcomeMsg.innerText = `welcome, ${userName}! enjoy JS`;
        welcomeMsg.style.color = "green";
    }
};

// Button-e click korle function-ta run hobe
greenBtn.addEventListener("click", showWelcomeMessage);