#!/usr/bin/node
// Importing the process module
const process = require('process');

// Printing process.argv property value
var args = process.argv;
// print process.argv
args.forEach((val, index) => {
  console.log(`${index}: ${val}`);
});
