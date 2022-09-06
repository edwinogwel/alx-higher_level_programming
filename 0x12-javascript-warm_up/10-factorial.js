#!/usr/bin/node
function factorial (n) {
  if (n > 1) {
    return n * factorial(n - 1); // factorial(1) = 1
  }
  if (n < 0) {
    return undefined;
  }
  return 1;
}
const x = parseInt(process.argv[2]);
console.log(factorial(x));
