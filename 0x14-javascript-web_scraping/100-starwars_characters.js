#!/usr/bin/node
// script should be executed using the Node.js interpreter

const request = require('request');
// Import the 'request' module to simplify HTTP requests

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
// Construct the API URL based on the provided movie ID

request.get(url, (error, response, body) => {
  // Make a GET request to the specified URL
  if (error) {
    // Handle errors during the request
    console.log(error);
    return;
  }

  // Parse the JSON response
  const data = JSON.parse(body);

  // Extract character URLs from the movie data
  const characters = data.characters;

  // Iterate through character URLs and fetch/print each character's name
  for (const character of characters) {
    request(character, (error, response, body) => {
      // Make a GET request to each character URL
      if (error) {
        // Handle errors during character request
        console.log(error);
        return;
      }

      // Parse the JSON response for each character
      const characterData = JSON.parse(body);

      // Print the name of each character
      console.log(characterData.name);
    });
  }
});
