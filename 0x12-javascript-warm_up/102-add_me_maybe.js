#!/usr/bin/node

// Define a function called 'addMeMaybe' that calls another function with an incremented number
function addMeMaybe (number, theFunction) {
  // Increment the given number by 1 and call the provided function
  theFunction(++number);
}

// Make the 'addMeMaybe' function available for use in other modules
module.exports = {
  addMeMaybe
};
