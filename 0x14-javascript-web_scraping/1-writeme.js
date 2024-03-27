#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Get the filename and content from the command line arguments
const filename = process.argv[2];
const content = process.argv[3];

// Use the 'fs.writeFile()' method to write the content to the file
fs.writeFile(filename, content, 'utf-8', (error) => {
  // Check for error during the file write operation
  if (error) {
    console.log(error);
  }
});
