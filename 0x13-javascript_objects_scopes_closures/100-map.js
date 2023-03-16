#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const lis = [];
const len = list.length
for (let i = -1; i < len; i++) {
    lis.push(i);
}
const mul = list.map((x, i) =>  x * i);
console.log(mul);
