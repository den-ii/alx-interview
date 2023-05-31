#!/usr/bin/node
// const request = require("request");

let characters;

request(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  async function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const newBody = await body;
    characters = JSON.parse(newBody).characters;
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
);
