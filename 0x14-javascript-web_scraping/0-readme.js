#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  if (error) {
    console.error(error);
  } else if (content === null || content === undefined) {
    console.error("Empty content or unable to read the file.");
  } else {
    console.log(content);
  }
});
