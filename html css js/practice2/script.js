// Element gulo ke select kora
const ageInput = document.getElementById("ageInput");
const checkBtn = document.getElementById("checkBtn");
const message = document.getElementById("message");

// Button-e click korle ei kak gulo hobe
checkBtn.addEventListener("click", function() {
    let age = Number(ageInput.value);

    // condition check kora
    if (age >= 18) {
        message.innerText = "Your are an adult! can be voter.";
        message.style.color = 'green';
    } else if (age >= 13 && age < 18) {
        message.innerText = "Your are an teenager!.";
        message.style.color = "blue";
    } else if (age > 0) {
        message.innerText = "Your are an child!.";
        message.style.color = "orange";
    } else {
        message.innerText = "Input correct number!.";
        message.style.color = "red";
    }
})