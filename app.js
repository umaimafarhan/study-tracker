let taskList = document.getElementById("taskList");

// Load saved tasks when page opens
document.addEventListener("DOMContentLoaded", loadTasks);

function addTask() {
const input = document.getElementById("taskInput");
const task = input.value.trim();

if (task === "") return;

createTaskElement(task);
saveTask(task);

input.value = "";
}

function createTaskElement(taskText) {
const li = document.createElement("li");
li.innerHTML = `
${taskText}
<span class="delete-btn" onclick="deleteTask(this)">✖</span>
`;
taskList.appendChild(li);
}

function deleteTask(element) {
const taskText = element.parentElement.textContent.replace("✖", "").trim();
deleteTaskFromStorage(taskText);
element.parentElement.remove();
}

function saveTask(task) {
let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
tasks.push(task);
localStorage.setItem("tasks", JSON.stringify(tasks));
}

function deleteTaskFromStorage(task) {
let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
tasks = tasks.filter(t => t !== task);
localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
tasks.forEach(createTaskElement);
}
