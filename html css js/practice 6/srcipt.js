const taskInput = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const taskList = document.getElementById("taskList");

// LocalStorage theke age thaka task gulo ana (jodi thake)
let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

// Page load howar sathe sathe tasks gulo screen-e dekhano
renderTasks();

// Add button-e click korle task add hobe
addBtn.addEventListener("click", function() {
    const taskText = taskInput.value.trim();

    if (taskText === "") {
        alert("Kichu ekta likho bhai!");
        return;
    }

    // Array-te notun task push kora
    tasks.push(taskText);

    // LocalStorage update kora
    updateLocalStorage();

    // UI render kora ebong input box clear kora
    renderTasks();
    taskInput.value = "";
});

// Tasks gulo screen-e display korar function
function renderTasks() {
    taskList.innerHTML = ""; // Age list clear kore newa

    tasks.forEach(function(task, index) {
        const li = document.createElement("li");
        li.innerText = task;

        // Delete button banano proti-ti task-er jonno
        const deleteBtn = document.createElement("button");
        deleteBtn.innerText = "Delete";
        
        // Delete button-er kaj
        deleteBtn.addEventListener("click", function() {
            tasks.splice(index, 1); // Array theke task remove kora
            updateLocalStorage();     // LocalStorage update kora
            renderTasks();            // Screen refresh kora
        });

        li.appendChild(deleteBtn);
        taskList.appendChild(li);
    });
}

// LocalStorage-e data save rakhar function
function updateLocalStorage() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}