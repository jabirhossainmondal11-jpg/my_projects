// Array of techlnologies
const techlnologies = ["HTML", "CSS", "JAVASCRIPT", "TYPESCRIPT", "REACT", "NEXT.JS"];

const techList = document.getElementById("techList");
const showBtn = document.getElementById("showBtn");

showBtn.addEventListener("click", function() {
    //Button e click korle list age clean kore neya valo
    techList.innerHTML = "";
    
    // Loop chalano array-er upore
    for (let i = 0; i < techlnologies.length; i++) {
        // ntun 'li' element create kora
        const li = document.createElement("li");

        // Array-er current item-ti li-te bosano
        li.innerText = techlnologies[i];

        //ul-er vitore li-ti jog kora (append kora)
        techList.append(li);
    }
})