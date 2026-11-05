//Element gulo select kora
const card = document.getElementById("card");
const desc = document.getElementById("desc");
const toggleBtn = document.getElementById("toggleBtn");

// Ekta variable track rakhar jonno je dark mode-e ache kina
let isDarkMode = false;

// Button-e click event add kora
toggleBtn.addEventListener("click", function() {
    if (isDarkMode === false) {
        //Dark mode active kora
        card.style.backgroundColor = "#222";
        card.style.color = "#fff";
        desc.innerText = "Ekhon Dark mode cholche!";
        toggleBtn.innerText = "Light Mode koro";
        isDarkMode = true;
    } else {
        //light mode-e fire jawa
        card.style.backgroundColor = "#fff";
        card.style.color = "#000";
        desc.innerText = "Ekhon Light mode cholche.";
        toggleBtn.innerText = "Dark Mode koro";
        isDarkMode = false;
    }
});