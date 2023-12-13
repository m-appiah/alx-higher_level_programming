#!/usr/bin/node
// Write a script that computes and prints a factorial

const input = parseInt(process.argv[2]);

function computeFactorial (input) {
  if (!input) { return 1; }

  if (input <= 0) { return; }
  return computeFactorial(input - 1) * input;
}
console.log(computeFactorial(input));
