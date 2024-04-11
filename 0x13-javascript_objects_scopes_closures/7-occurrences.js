#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const item of list) {
    count = item === searchElement ? count + 1 : count;
  }
  return (count);
};
