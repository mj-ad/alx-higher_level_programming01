#!/usr/bin/node
const process = require('process');
const first = process.argv[2];
const second = process.argv[3];
if (typeof first !== undefined && typeof second !== undefined) {
  console.log(first + ' is ' + second);
} else if (typeof first !== undefined && typeof second === undefined) {
  console.log(first + ' is undefined');
}else {
  console.log('undefined is undefined');
}
