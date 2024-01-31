#!/usr/bin/node

// Import the 'request' module to simplify HTTP requests
const request = require('request');
// Get the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the specified URL with JSON response parsing
request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
// Create an object to store the count of completed tasks for each user
  const tasksCompleted = {};
// Iterate through the todos to count completed tasks by user
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
