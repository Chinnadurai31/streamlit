import streamlit as st

st.title("🐍 Snake Game in Streamlit")

# Embedding the Snake game using HTML and JavaScript
snake_game = """
<html>
  <head>
    <style>
      body { margin: 0; }
      canvas { display: block; margin: auto; background-color: #000; }
    </style>
  </head>
  <body>
    <canvas id="gameCanvas"></canvas>
    <script>
      const canvas = document.getElementById("gameCanvas");
      const ctx = canvas.getContext("2d");

      const grid = 20;
      let count = 0;

      let snake = {
        x: grid * 5,
        y: grid * 5,

        // snake velocity. moves one grid length every frame in either the x or y direction
        dx: grid,
        dy: 0,

        // keep track of all grids the snake body occupies
        cells: [],

        // length of the snake. grows when eating an apple
        maxCells: 4
      };
      let apple = {
        x: grid * 10,
        y: grid * 10
      };

      // get random whole numbers in a specific range
      // @see https://stackoverflow.com/a/1527820/2124254
      function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min)) + min;
      }

      // game loop
      function loop() {
        requestAnimationFrame(loop);

        // slow game loop to 15 fps instead of 60 - 60/15 = 4
        if (++count < 4) {
          return;
        }

        count = 0;
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // move snake by its velocity
        snake.x += snake.dx;
        snake.y += snake.dy;

        // wrap snake position horizontally on edge of screen
        if (snake.x < 0) {
          snake.x = canvas.width - grid;
        } else if (snake.x >= canvas.width) {
          snake.x = 0;
        }

        // wrap snake position vertically on edge of screen
        if (snake.y < 0) {
          snake.y = canvas.height - grid;
        } else if (snake.y >= canvas.height) {
          snake.y = 0;
        }

        // keep track of where snake has been. front of the array is always the head
        snake.cells.unshift({ x: snake.x, y: snake.y });

        // remove cells as we move away from them
        if (snake.cells.length > snake.maxCells) {
          snake.cells.pop();
        }

        // draw apple
        ctx.fillStyle = "red";
        ctx.fillRect(apple.x, apple.y, grid - 1, grid - 1);

        // draw snake one cell at a time
        ctx.fillStyle = "green";
        snake.cells.forEach(function (cell, index) {

          ctx.fillRect(cell.x, cell.y, grid - 1, grid - 1);

          // snake ate apple
          if (cell.x === apple.x && cell.y === apple.y) {
            snake.maxCells++;

            // canvas is 400x400 which is 20x20 grids
            apple.x = getRandomInt(0, 20) * grid;
            apple.y = getRandomInt(0, 20) * grid;
          }

          // check collision with all cells after this one (modified bubble sort)
          for (let i = index + 1; i < snake.cells.length; i++) {

            // snake occupies same space as a body part. reset game
            if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
              snake.x = grid * 5;
              snake.y = grid * 5;
              snake.cells = [];
              snake.maxCells = 4;
              snake.dx = grid;
              snake.dy = 0;

              apple.x = getRandomInt(0, 20) * grid;
              apple.y = getRandomInt(0, 20) * grid;
            }
          }
        });
      }

      // listen to keyboard events to move the snake
      document.addEventListener("keydown", function (e) {
        // prevent snake from backtracking on itself by checking that it's
        // not already moving on the same axis (pressing left while moving
        // left won't do anything, and pressing right while moving left
        // shouldn't let you collide with your own body)

        // left arrow key
        if (e.which === 37 && snake.dx === 0) {
          snake.dx = -grid;
          snake.dy = 0;
        }
        // up arrow key
        else if (e.which === 38 && snake.dy === 0) {
          snake.dy = -grid;
          snake.dx = 0;
        }
        // right arrow key
        else if (e.which === 39 && snake.dx === 0) {
          snake.dx = grid;
          snake.dy = 0;
        }
        // down arrow key
        else if (e.which === 40 && snake.dy === 0) {
          snake.dy = grid;
          snake.dx = 0;
        }
      });

      // set up the canvas
      canvas.width = 400;
      canvas.height = 400;

      // start the game loop
      requestAnimationFrame(loop);
    </script>
  </body>
</html>
"""

# Display the game using Streamlit's components
st.components.v1.html(snake_game, height=500)
