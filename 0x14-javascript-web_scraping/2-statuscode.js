#!/usr/bin/node
// The shebang line specifies that this script should be executed using the Node.js interpreter

const request = require('request');
// Import the 'request' module to simplify HTTP requests
const url = process.argv[2];
// Get the URL from the command line arguments

request.get(url, (error, response) => {
  // Make a GET request to the specified URL
  if (error) {
    // Handle errors
    console.log(error);
  } else {
    // Print the status code of the response
    console.log(`code: ${response.statusCode}`);
  }
});
