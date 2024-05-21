#!/usr/bin/node
const req = require('request');
req(process.argv[2], (err, res, data) => {
  if (err) console.log(err);
  else {
    const obj = {};
    JSON.parse(data).forEach(({ completed, userId }) => {
      if (completed && obj[userId]) obj[userId]++;
      else if (completed) obj[userId] = 1;
    });
    console.log(obj);
  }
});
