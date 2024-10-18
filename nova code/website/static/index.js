//function for deleting tasks
function deleteTask(taskId) {
  //establishes the function
  fetch("/delete-task", {
    method: "POST",
    //the function is sent to the server as a JSON string
    body: JSON.stringify({ taskId: taskId }),
    //the rest of the function returns the URL of the loaded page
  }).then((_res) => {
    window.location.href = "/";
  });
}
