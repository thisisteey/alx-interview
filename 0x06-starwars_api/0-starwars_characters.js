#!/usr/bin/node
const request = require('request');
const starWarsAPI = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${starWarsAPI}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charAPIurls = JSON.parse(body).characters;
    const charNames = charAPIurls.map(
      charUrl => new Promise((resolve, reject) => {
        request(charUrl, (charErr, __, charBody) => {
          if (charErr) {
            reject(charErr);
          }
          resolve(JSON.parse(charBody).name);
        });
      }));

    Promise.all(charNames)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
