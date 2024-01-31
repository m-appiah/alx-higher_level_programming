#!/usr/bin/node
// The shebang line specifies that this script should be executed using the Node.js interpreter

const fs = require('fs');
// Import the 'fs' (file system) module to work with file operations
const filename = process.argv[2];
// Get the filename from the command line arguments

fs.readFile(filename, 'utf-8', (error, content) => {
  // Read the file asynchronously in utf-8 encoding
  if (error) {
    // Handle errors
    console.log(error);
  } else {
    // Print the file content
    console.log(content);
  }
});
