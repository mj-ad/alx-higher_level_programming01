#!/usr/bin/node
const process = require('process');
function factorial (a) {
  let prod = a
  while (a > 1) {
    a--;
    prod = prod * a;
  }
  console.log(prod);
}

const num = process.argv[2];
if (isNaN(num) || typeof num === 'undefined') {
  console.log('1');
} else {
  const arg = parseInt(num);
  factorial(arg);
}
