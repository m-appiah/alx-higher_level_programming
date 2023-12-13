#!/usr/bin/node
// Write a script that concats 2 files.

const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');
const contentC = contentA + '\n' + contentB;

fs.writeFileSync(fileC, contentC);
