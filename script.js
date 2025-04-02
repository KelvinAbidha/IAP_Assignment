// Query & store input and button elements
const newTask = document.getElementById("task");
const submit = document.getElementById("submit");
const taskList = document.getElementById("task-list");

// Enable the button when the input field is not empty
newTask.addEventListener("input", () => {
    if (newTask.value.trim() !== "") {
        submit.disabled = false; // Enable the button
    } else {
        submit.disabled = true; // Disable the button
    }
});

// Add task to the list when the form is submitted
document.getElementById("todo-form").onsubmit = (event) => {
    // Prevent default form submission
    event.preventDefault(); // Prevents the form from reloading the page

    // Create a new list item
    const li = document.createElement("li");
    li.textContent = newTask.value;

    // Add the new task to the list
    taskList.appendChild(li);

    // Clear the input field and disable the button
    newTask.value = "";
    submit.disabled = true;
};