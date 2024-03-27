#!/usr/bin/node
// The shebang line specifies that this script should be executed using the Node.js interpreter

const request = require('request');
// Import the 'request' module to simplify HTTP requests
const movieId = process.argv[2];
// Get the movie ID from the command line arguments
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
// Construct the API URL based on the provided movie ID

request.get(url, (error, response, body) => {
  // Make a GET request to the specified URL
  if (error) {
    // Handle errors
    console.log(error);
  } else {
    // Parse the JSON response
    const data = JSON.parse(body);

    // Print the title of the movie
    console.log(data.title);
  }
});
