#!/usr/bin/node
// The shebang line specifies that this script should be executed using the Node.js interpreter

const request = require('request');
// Import the 'request' module to simplify HTTP requests
const url = process.argv[2];
// Get the URL from the command line arguments
const characterId = '18';
let count = 0;
// Make a GET request to the specified URL and Handle errors
request.get(url, (error, response, body) => {
	if (error) {
		console.log(error);
	} else {
		// Parse the JSON response
		const data = JSON.parse(body);

		// Loop through the films and characters to count appearances of the specified character
		data.results.forEach((film) => {
			film.characters.forEach((character) => {
				if (character.includes(characterId)) {
					count += 1;
				}
			});
		});

		// Print the count
		console.log(count);
	}
});
