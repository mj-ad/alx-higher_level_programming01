#!/usr/bin/node
const process = require('process');
function add (a, b) {
  console.log(a + b);
}
const first = process.argv[2];
const second = process.argv[3];
if (isNaN(first) || typeof first === 'undefined') {
  console.log('NaN');
} else if (isNaN(second) || typeof second === 'undefined') {
  console.log('NaN');
} else {
  const a = parseInt(first);
  const b = parseInt(second);
  add(a, b);
}
