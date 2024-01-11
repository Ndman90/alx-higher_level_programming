#!/usr/bin/node
/**
 * Check the parameters provided
 */
class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      // Initialize instance attributes
      this.width = w;
      this.height = h;
    } else {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      this.width = 0;
      this.height = 0;
    }
  }

  // Instance method to print the rectangle using 'X'
  print () {
    if (this.width === 0 || this.height === 0) {
      console.log('Empty Rectangle');
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Rectangle;
