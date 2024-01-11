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
}
module.exports = Rectangle;
