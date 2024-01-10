#!/usr/bin/node

function add (a, b) {
  return a + b;
}

// Make the 'add' function available for use in other modules
module.exports = {
  add
};
