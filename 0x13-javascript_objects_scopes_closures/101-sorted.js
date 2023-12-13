#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const { dict } = require('./101-data');

const invertedDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!invertedDict[occurrences]) {
    invertedDict[occurrences] = [];
  }
  invertedDict[occurrences].push(userId);
}

console.log(invertedDict);
