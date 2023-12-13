#!/usr/bin/node
// Write a script that prints x times “C is fun”

const x = parseInt(process.argv[2]);
const c = 'C is fun';

if (!isNaN(x) && x > 0) {
  for (let i = 0; i < x; i++) {
    console.log(c);
  }
} else {
  console.log('Missing number of occurrences');
}
