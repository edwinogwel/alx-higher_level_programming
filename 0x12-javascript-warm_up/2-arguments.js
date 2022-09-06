#!/usr/bin/node
const messages = ['No argument', 'Argument found', 'Arguments found'];
console.log(messages[Math.min(process.argv.length - 2, 2)]);
