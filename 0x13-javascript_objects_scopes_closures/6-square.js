#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
};
