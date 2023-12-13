#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  const uniqueValues = [...new Set(args)];
  if (uniqueValues.length === 1) {
    console.log(uniqueValues[0]);
  } else {
    console.log(uniqueValues[1]);
  }
}
