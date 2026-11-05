// Html element gulo ke select kora
const MyH1 = document.getElementById("myH1");
const bTn = document.getElementById("btn");

//Button-e click korle ki hobe ta bole dewa (Event Listener)
bTn.addEventListener("click", function() {
    MyH1.innerText = "JavaScript is used";
    MyH1.style.color = "crimson";
    MyH1.style.fontSize = "32px";
});
