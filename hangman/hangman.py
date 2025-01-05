import random

class DrawingHangman:
  def __init__ (self, wordbank):
    self.attempts = 0
    self.secret_word = random.choice(wordbank)
    self.guessed_letters = []

  def is_letter_in_secret_word (self, guess):
    self.guessed_letters.append(guess)
    if guess in self.secret_word:
      return True
    else:
      return False

  def draw_word (self, turtle):
    for letter in self.secret_word:
      if letter in self.guessed_letters:
        turtle.write(letter, None, "center", "16pt")
        turtle.penup()
        turtle.forward(25)
      else:
        turtle.pendown()
        turtle.forward(25)
        turtle.penup()
        turtle.forward(15)
