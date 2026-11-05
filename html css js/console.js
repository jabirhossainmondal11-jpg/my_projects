//variable declaration
const siteName = "My Awesome website";
let visitorCount = 45;

console.log("website Name:", siteName);
console.log("Initial Visitors:", visitorCount);

//visitor count update kora
visitorCount = 46;
console.log("Upadated Visitors:", visitorCount);

/*// Function declare 
function sayHello(name) {
    console.log("Hello, " + name +'! is JavaScript ok?');

};

//Function calling
sayHello("Jabir");
sayHello("simran");*/

/*//moder style to write function(arrow function):
// a function to add two numbers
const addNumbers = (num1, num2) => {
    return num1 + num2;
};

let result = addNumbers(11, 20);
console.log("jogfol:", result);*/

/*// suntax: (intialization; condition; increament/decrement)

for (let i = 1; i <= 5; i++) {
    console.log("current Number: " + i)
}*/

/*// ekti user object
const user = {
    name: "Jabir Hossain",
    age: 17,
    skills: ["HTML", "CSS", "JAVASCRIPT"],
    isDeveloper: true,

    //object=er bhitore function ba method thakte pare
    greet: function() {
        console.log("Hello! my name is " + this.name);
    }
};
// Object theke data access kora
console.log(user.name);
console.log(user.skills[1]);

// Method call kora
user.greet();*/

/*const numbers = [1, 2, 3, 4, 5, 6];

// 1. map(): proti-ti number ke 3 diye multiply kora
const multiplied = numbers.map(num => num * 3);
console.log("Multiplied", multiplied);

// 2. filter(): shudhu even number gulo ke filter kora
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log("Even Numbers: ", evenNumbers);*/

/*// Ekta async function declare kora
async function fetchUserData() {

    try {
        console.log("Data ana hocche, ektu opekha koro...");
        // fetch() diye server theke data request kora
        const response = await fetch('https://jsonplaceholder.typicode.com/users/1')

        //response ke usable JSON format-e convert kora
        const data = await response.json();

        console.log("server thke pawa Data: ", data);
        console.log("User-er Name: ", data.name);
        console.log("User-er Email :, data.email");

    }   catch (error) {
        // kono network error ba somossa hole eta catch korbe
        console.log("Kono error hoyeche: ", error );
    } 
}

// Function call kora
fetchUserData();*/
