#!/usr/bin/node
const req = require('request');
function getUsers (chs, idx = 0) {
  if (idx >= chs.length) return;
  console.log(chs.length, idx);
  req(chs[idx], (err, res, data) => {
    if (!err) {
      console.log(JSON.parse(data).name);
      getUsers(chs, idx + 1);
    }
  });
}
req(
    `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
    (err, res, data) => {
      if (err) console.log(err);
      else {
        getUsers(JSON.parse(data).characters);
      }
    }
);
