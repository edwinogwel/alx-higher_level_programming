#!/usr/bin/node
const x = parseInt(process.argv[2]); // argv[2] -> 1st arg
if (Number.isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
