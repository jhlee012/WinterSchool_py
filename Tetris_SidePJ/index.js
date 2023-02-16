/**
 * @author jhlee012
 *
 */

// Settings

const GAME_ROWS  = 20;
const GAME_COLS = 10;

// variables
let score = 0;
let duration = 500;
let downInterval;
let tempMovingite;


const BLOCK = {
  tree: [
      
  ]
}


const playground = document.querySelector('.playground > ul')

for (let i = 0; i < 20; i++) { // 0~19
  const li = document.createElement('li')
  const ul = document.createElement('ul')

  for (let j = 0; j < 10; j++) {
    const matrix = document.createElement('li')
    ul.prepend(matrix)
  }
  li.prepend(ul)
  playground.prepend(li)
}