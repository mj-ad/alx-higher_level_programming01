#!/usr/bin/node
const process = require('process');
const str = process.argv[2];
const arg = parseInt(str);
if (typeof str === 'undefined') {
  console.log('Missing number of occurrences');
} else {
  for (let num = 1; num <= arg; num++) {
    console.log('C is fun');
  }
}
