#!/usr/bin/node
const req = require('request');
req('https://swapi-api.alx-tools.com/api/films/', (err, res) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(res.body);
  console.log(
    data.results.reduce((prev, data) => {
      if (
        data?.characters.includes(
          'https://swapi-api.alx-tools.com/api/people/18/'
        )
      ) { return prev + 1; } else return prev;
    }, 0)
  );
});
