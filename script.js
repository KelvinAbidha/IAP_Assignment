const newTask = document.getElementById("newTask");
const submit = document.getElementById("submit");
const taskList = document.getElementById("taskList");

newTask.addEventListener("input", () => submit.disabled = !newTask.value.trim());

document.getElementById("taskForm").addEventListener("submit", e => {
    e.preventDefault();
    const task = document.createElement("li");
    task.textContent = newTask.value.trim();
    taskList.append(task);
    newTask.value = "";
    submit.disabled = true;
});
