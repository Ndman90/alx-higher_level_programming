#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < size; row++) {
    let rowContent = '';
    for (let column = 0; column < size; column++) {
      rowContent += 'X';
    }
    console.log(rowContent);
  }
}
