#!/usr/bin/node
const process = require('process');
const len = process.argv.length;
if (len > 3) {
  console.log('Arguments found');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
