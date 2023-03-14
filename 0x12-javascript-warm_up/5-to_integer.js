#!/usr/bin/node
const process = require('process');
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  const num = parseInt(arg);
  console.log('My number: ' + num);
}
