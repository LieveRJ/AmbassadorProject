from turtle import *
from hangman import DrawingHangman

import turtle
import time 

# Set up the screen
screen = turtle.Screen()
screen.title("Hangman Game")
screen.bgcolor("white")
screen.setup(width=700, height=700)

word_turtle = turtle.Turtle()
figure_turtle = turtle.Turtle()
game = DrawingHangman()

# Create game loop
while not game.terminate:
  # Set-up the turtle that will be drawing the guessed word
  word_turtle.shape("turtle")
  word_turtle.speed(7)
  word_turtle.penup()
  word_turtle.goto(-120, -120)

  # Set-up the turtle that will be drawing the stick man
  figure_turtle.penup()
  figure_turtle.goto(0, 300)
  figure_turtle.color("blue")
  figure_turtle.write("Let's play Hangman, guess the letters!", None, "center", font = ("Arial", 20, "bold"))
  figure_turtle.color("black")

  # Play the hangman game
  game.play_hangman(word_turtle, figure_turtle)
  
  # Give player 5 seconds to see the result
  figure_turtle.goto(0, -50)
  figure_turtle.write('Wait 5 seconds to play again.', False, align = 'center', font = ("Arial", 10, "normal"))
  time.sleep(5)

  # Clear the turtles
  word_turtle.clear()
  figure_turtle.clear()
  game = DrawingHangman()