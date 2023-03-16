#!/usr/bin/node
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  constructor (size) {
    super(size);
    this.size = size;
  }
  charPrint (c) {
    let str = '';
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (c === undefined) {
          c = 'X';
	}
        str += c;
      }
      console.log(str);
      str = '';
    }
  }
};
