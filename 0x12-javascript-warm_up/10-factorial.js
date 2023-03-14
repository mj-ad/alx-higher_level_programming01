#!/usr/bin/node
const process = require('process');
function factorial (a) {
  if (isNaN(a) || typeof a === 'undefined' || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const num = process.argv[2];
const arg = parseInt(num);
console.log(factorial(arg));
