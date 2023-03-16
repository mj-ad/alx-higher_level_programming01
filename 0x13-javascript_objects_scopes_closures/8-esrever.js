#!/usr/bin/node
exports.esrever = function (list) {
  const list1 = [];
  const len = list.length;
  for (let i = (len - 1); i >= 0; i--) {
    list1.push(list[i]);
  }
  return list1;
};
