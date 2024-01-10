#!/usr/bin/node

// Check if there are enough command-line arguments
if (process.argv.length <= 3) {
  console.log(0);
} else {
  /* Convert command-line arguments to numbers, remove script name and interpreter */
  const numbers = process.argv.slice(2).map(Number);

  // Sort the numbers in ascending order
  const sortedNumbers = numbers.sort((a, b) => a - b);

  // Find and print the second-to-last number
  const secondToLast = sortedNumbers[sortedNumbers.length - 2];
  console.log(secondToLast);
}
