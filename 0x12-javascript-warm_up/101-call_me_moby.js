#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  while (x) {
    x--;
    theFunction();
  }
};

