#!/usr/bin/node
// script should be executed using the Node.js interpreter

const request = require('request');
// Import the 'request' module to simplify HTTP requests

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
let chars = [];
// Initialize an array to store character URLs

request(url, (error, response, body) => {
  // Make a GET request to the specified URL
  if (error) {
    // Handle errors during the request
    console.log(error);
    return;
  }

  // Parse the JSON response
  const data = JSON.parse(body);

  // Extract character URLs from the movie data
  chars = data.chars;

  // Call the getCharacters function to start fetching and printing characters
  getCharacters(0);
});

// Recursive function to fetch and print characters
const getCharacters = (index) => {
  // Base case: Stop recursion when the index reaches the end of the character list
  if (index === chars.length) {
    return;
  }

  // Make a GET request to each character URL
  request(chars[index], (error, response, body) => {
    if (error) {
      // Handle errors during character request
      console.log(error);
      return;
    }

    // Parse the JSON response for each character
    const charData = JSON.parse(body);

    // Print the name of each character
    console.log(charData.name);

    // Recursively call the function to fetch and print the next character
    getCharacters(index + 1);
  });
};
