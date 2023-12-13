#!/usr/bin/node
// Write a script that prints a square

const size = process.argv[2];

if (size && parseInt(size)) {
  let i = 0;
  while (i < size) {
    const row = 'X'.repeat(size);
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
