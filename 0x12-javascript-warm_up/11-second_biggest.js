#!/usr/bin/node
const process = require('process');
const len = process.argv.length;
if (len < 4) {
  console.log(0);
} else {
  const array = process.argv.slice(2, len);
  array.sort(function (a, b) { return a - b; });
  console.log(array[(array.length - 2)]);
}
