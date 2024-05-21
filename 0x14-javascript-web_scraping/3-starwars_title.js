#!/usr/bin/node
const req = require('request');
req('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, res) => console.log(err || JSON.parse(res.body).title));
