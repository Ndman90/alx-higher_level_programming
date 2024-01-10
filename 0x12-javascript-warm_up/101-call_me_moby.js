#!/usr/bin/node

// Define a function called 'callMeMoby' that repeats the provided function 'x' times
function callMeMoby (x, theFunction) {
  // Loop 'x' times
  for (let i = 0; i < x; i++) {
    // Call the provided function
    theFunction();
  }
}

// Make the 'callMeMoby' function available for use in other modules
module.exports = {
  callMeMoby
};
