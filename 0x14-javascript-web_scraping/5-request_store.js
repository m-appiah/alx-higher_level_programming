#!/usr/bin/node
// script should be executed using the Node.js interpreter

const request = require('request');
// Import the 'request' module to simplify HTTP requests
const fs = require('fs');
// Import the 'fs' module to work with file operations
const url = process.argv[2];
// Get the URL from the command line arguments
const file = process.argv[3];
// Get the file path from the command line arguments

request(url, (error, response, body) => {
	// Make a GET request to the specified URL
	if (error) {
		// Handle errors during the request
		console.log(error);
	} else {
		// Write the body content to the specified file
		fs.writeFile(file, body, 'utf8', (error) => {
			if (error) {
				// Handle errors during file writing
				console.log(error);
			}
		});
	}
});
