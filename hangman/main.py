from turtle import *
from hangman import *

import turtle
import time

delay = 0.5
wordbank = ['affix', 'bagpipes', 'bandwagon', 'banjo', 'buffalo',
            'cobweb', 'croquet', 'daiquiri', 'duplex', 'dwarves',
            'equip', 'exodus', 'fishhook', 'fixable', 'galaxy',
            'galvanize', 'ivy', 'juicy', 'kilobyte', 'megahertz',
            'oxygen', 'polka', 'quiz', 'rhubarb', 'schizophrenia',
            'unzip', 'uptown', 'vodka', 'whiskey', 'zombie']


# Set up the screen
screen = turtle.Screen()
screen.title("Hangman Game")
screen.bgcolor("white")
screen.setup(width=700, height=700)

hangman_word = turtle.Turtle()
hangman_word.shape("turtle")
hangman_word.speed(7)
hangman_word.penup()

text = turtle.Turtle()
text.penup()
text.goto(0, 150)
text.write("Let's play Hangman, guess the letters!", None, "center", "16pt")
text.goto(0, 100)

game = DrawingHangman(wordbank)

hangman_word.goto(-120, -120)
game.draw_word(hangman_word)


while True:
  guess  = turtle.textinput("Hangman game", "Guess a letter...")
  if len(guess) > 1 or not guess.isalpha():
      print("Only single letters are allowed.")
  guess = guess.lower()
  game.is_letter_in_secret_word(guess)
  hangman_word.clear()
  hangman_word.goto(-120, -120)
  game.draw_word(hangman_word)

  time.sleep(delay)