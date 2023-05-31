#!/usr/bin/node
const request = require('request');

if (!process.argv[2] || process.argv[2] == 0 || !Number(process.argv[2])) {
  console.log('Please input arg');
} else {
  request(
    'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
    async function (error, response, body) {
      if (error) {
        console.log(error);
      }
      const newBody = await body;
      const characters = JSON.parse(newBody).characters;
      if (characters && characters.length) {
        characters.forEach((element) => {
          request(element, async function (error, response, body) {
            if (error) {
              console.log(error);
            }
            const newBody = await body;
            console.log(JSON.parse(newBody).name);
          });
        });
      }
    });
}
