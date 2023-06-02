#!/usr/bin/node
const request = require('request');

if (!process.argv[2]) {
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
      // console.log(characters);
      if (characters && characters.length) {
        for (const character of characters) {
          const ll = await new Promise((resolve, reject) => {
            request(character, async function (error, response, body) {
              if (error) {
                reject(error);
              }
              const newBody = await body;
              resolve(JSON.parse(newBody).name);
            });
          });
          console.log(ll);
        }
      }
    }
  );
}
