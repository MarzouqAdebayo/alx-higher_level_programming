#!/usr/bin/node
exports.callMeMoby = function (x, fn) {
  while (x > 0) {
    fn();
    x--;
  }
};
