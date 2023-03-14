#!/usr/bin/node
const process = require('process');
const str = process.argv[2];
if (isNaN(str) || typeof str === 'undefined') {
  console.log('Missing size');
} else {
  const arg = parseInt(str);
  let s = '';
  for (let size = 0; size < arg; size++) {
    for (let width = 0; width < arg; width++) {
      s += 'X';
    }
    console.log(s);
    s = '';
  }
}
